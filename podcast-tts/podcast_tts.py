#!/usr/bin/env python3
"""
Podcast TTS Generator - ListenHub API Integration
根据播客脚本和角色音色配置，批量生成并合并播客音频
"""
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from typing import List, Tuple, Dict

# ListenHub API 配置
API_KEY = "填入用户提供的ListenHub API key"
API_URL = "https://api.listenhub.ai/openapi/v1/tts"
SPEAKERS_URL = "https://api.listenhub.ai/openapi/v1/speakers/list?language=zh"

# 分段配置
MAX_CHARS_PER_CHUNK = 1500


def get_chinese_speakers() -> List[Dict]:
    """获取 ListenHub 中文音色列表"""
    try:
        req = urllib.request.Request(
            SPEAKERS_URL,
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", {}).get("items", [])
    except Exception as e:
        print(f"获取音色列表失败: {e}")
        return []


def find_speaker_id(speaker_name: str, speakers: List[Dict]) -> str:
    """根据中文名查找音色 ID"""
    for s in speakers:
        if speaker_name in s.get("name", ""):
            return s.get("speakerId", "")
    return ""


def parse_script(file_path: str) -> List[Tuple[str, str]]:
    """
    解析播客脚本，返回 [(角色, 文本), ...] 列表
    支持格式：【角色名】标记
    """
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()

    segments = []
    current_role = None
    current_lines = []
    role_pattern = re.compile(r"^【(.+?)】\s*$")

    for line in raw.splitlines():
        m = role_pattern.match(line.strip())
        if m:
            # 保存上一个角色的内容
            if current_role and current_lines:
                text = "\n".join(l for l in current_lines if l.strip())
                if text.strip():
                    segments.append((current_role, text.strip()))
            # 开始新角色
            current_role = m.group(1)
            current_lines = []
        else:
            if current_role is not None:
                current_lines.append(line)

    # 保存最后一个角色
    if current_role and current_lines:
        text = "\n".join(l for l in current_lines if l.strip())
        if text.strip():
            segments.append((current_role, text.strip()))

    return segments


def split_long_text(text: str, max_chars: int) -> List[str]:
    """按句号/问号/感叹号切分长文本，保持句子完整"""
    if len(text) <= max_chars:
        return [text]

    sentences = re.split(r"(?<=[。！？])\s*", text)
    sentences = [s for s in sentences if s.strip()]

    chunks = []
    buf = ""
    for s in sentences:
        if len(buf) + len(s) <= max_chars:
            buf += s
        else:
            if buf:
                chunks.append(buf)
            # 如果单句超长，强制切分
            if len(s) > max_chars:
                for i in range(0, len(s), max_chars):
                    chunks.append(s[i:i + max_chars])
                buf = ""
            else:
                buf = s
    if buf:
        chunks.append(buf)

    return chunks


def synthesize_audio(text: str, voice_id: str, output_path: str, retries: int = 3) -> bool:
    """调用 ListenHub API 生成音频"""
    payload = {"input": text, "voice": voice_id}
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=180) as resp:
                content_type = resp.headers.get("content-type", "")
                body = resp.read()

            # 检查是否返回音频
            if "audio" not in content_type:
                try:
                    err = json.loads(body.decode("utf-8"))
                    print(f"    API 错误: {err.get('message', err)}")
                except Exception:
                    print(f"    非音频响应: {body[:200]}")
                if attempt < retries:
                    time.sleep(3 * attempt)
                    continue
                return False

            # 保存音频文件
            with open(output_path, "wb") as f:
                f.write(body)
            return True

        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")[:300]
            print(f"    HTTP {e.code}: {err_body}")
            if e.code == 429:  # Rate limit
                print(f"    限流，等待 8 秒后重试 ({attempt}/{retries})")
                time.sleep(8)
            else:
                time.sleep(3 * attempt)
        except Exception as e:
            print(f"    异常: {e}")
            time.sleep(3 * attempt)

    return False


def merge_audio_files(file_list: List[str], output_path: str) -> bool:
    """使用 ffmpeg 合并音频文件"""
    import subprocess

    # 创建 ffmpeg concat 文件列表
    list_file = output_path.replace(".mp3", "_filelist.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for file_path in file_list:
            f.write(f"file '{os.path.basename(file_path)}'\n")

    # 执行 ffmpeg 合并
    try:
        cmd = [
            "ffmpeg", "-f", "concat", "-safe", "0",
            "-i", os.path.basename(list_file),
            "-c", "copy",
            os.path.basename(output_path),
            "-y"  # 覆盖已存在文件
        ]
        result = subprocess.run(
            cmd,
            cwd=os.path.dirname(output_path),
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            return True
        else:
            print(f"ffmpeg 错误: {result.stderr}")
            return False
    except Exception as e:
        print(f"合并失败: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("用法: python podcast_tts.py <脚本文件> [输出目录]")
        print("示例: python podcast_tts.py script.txt output/")
        sys.exit(1)

    script_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # 自动生成输出目录
    if not output_dir:
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        output_dir = os.path.join(
            os.path.dirname(script_path),
            f"{script_name}_ListenHub"
        )

    os.makedirs(output_dir, exist_ok=True)

    print(f"📄 脚本文件: {script_path}")
    print(f"📁 输出目录: {output_dir}\n")

    # 获取音色列表
    print("🎤 获取 ListenHub 中文音色列表...")
    speakers = get_chinese_speakers()
    if not speakers:
        print("❌ 无法获取音色列表，请检查网络和 API Key")
        sys.exit(1)
    print(f"✓ 找到 {len(speakers)} 个中文音色\n")

    # 解析脚本
    print("📖 解析播客脚本...")
    segments = parse_script(script_path)
    if not segments:
        print("❌ 脚本为空或格式错误")
        sys.exit(1)

    roles = list(set(role for role, _ in segments))
    print(f"✓ 识别到 {len(segments)} 个段落，{len(roles)} 个角色: {', '.join(roles)}\n")

    # 这里需要用户提供角色到音色的映射
    # 在实际使用时，这部分会由 Claude 根据用户指令动态生成
    print("⚠️  请在调用此脚本前设置 VOICE_MAP 环境变量")
    print("示例: export VOICE_MAP='{\"旁白\":\"CN-Man-Beijing-V2\",\"主持人\":\"chat-girl-105-cn\"}'")

    # 从环境变量读取音色映射
    voice_map_str = os.environ.get("VOICE_MAP", "{}")
    try:
        voice_map = json.loads(voice_map_str)
    except Exception:
        print("❌ VOICE_MAP 格式错误")
        sys.exit(1)

    if not voice_map:
        print("❌ 未设置音色映射")
        sys.exit(1)

    print(f"🎵 音色映射: {voice_map}\n")

    # 生成音频计划
    plan = []
    for role, text in segments:
        voice_id = voice_map.get(role)
        if not voice_id:
            print(f"⚠️  角色 '{role}' 未配置音色，跳过")
            continue
        chunks = split_long_text(text, MAX_CHARS_PER_CHUNK)
        for chunk in chunks:
            plan.append((role, voice_id, chunk))

    print(f"🎬 生成计划: {len(plan)} 个音频片段\n")

    # 批量生成音频
    audio_files = []
    success_count = 0

    for idx, (role, voice_id, text) in enumerate(plan, 1):
        safe_role = role.replace(" ", "").replace("/", "_")
        filename = f"{idx:03d}_{safe_role}.mp3"
        output_path = os.path.join(output_dir, filename)

        preview = text[:30].replace("\n", " ")
        print(f"[{idx:03d}/{len(plan)}] {role} ({voice_id}) {len(text)} 字")
        print(f"  {preview}...")

        if synthesize_audio(text, voice_id, output_path):
            size_kb = os.path.getsize(output_path) / 1024
            print(f"  ✓ {filename} ({size_kb:.1f} KB)\n")
            audio_files.append(output_path)
            success_count += 1
        else:
            print(f"  ✗ {filename} 生成失败\n")

        # 避免触发限流
        time.sleep(1.0)

    print("=" * 60)
    print(f"✓ 完成: {success_count}/{len(plan)} 段成功\n")

    if success_count == 0:
        print("❌ 没有成功生成任何音频")
        sys.exit(1)

    # 合并音频
    script_name = os.path.splitext(os.path.basename(script_path))[0]
    merged_path = os.path.join(output_dir, f"{script_name}_完整版.mp3")

    print(f"🔗 合并音频文件...")
    if merge_audio_files(audio_files, merged_path):
        size_mb = os.path.getsize(merged_path) / (1024 * 1024)
        print(f"✓ 完整版播客: {merged_path} ({size_mb:.1f} MB)\n")
    else:
        print("⚠️  合并失败，但分段音频已生成\n")

    print(f"📁 输出目录: {output_dir}")


if __name__ == "__main__":
    main()
