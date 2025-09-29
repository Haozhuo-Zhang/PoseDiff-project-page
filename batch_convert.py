import os
import subprocess
from pathlib import Path

# 输入文件夹（你的视频目录）
INPUT_DIR = "./static/videos/alpha_old"
# 输出文件夹
OUTPUT_DIR = "./static/videos/alpha"

# ffmpeg 编码参数
VIDEO_CODEC = "h264"   # 如果你装了官方 ffmpeg，可以改成 "libx264"
AUDIO_CODEC = "aac"

# 支持的视频扩展名
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"}

def convert_video(input_path: Path, output_path: Path):
    """调用 ffmpeg 转码单个视频"""
    cmd = [
        "ffmpeg", "-y",   # -y 表示自动覆盖
        "-i", str(input_path),
        "-c:v", VIDEO_CODEC,
        "-c:a", AUDIO_CODEC,
        "-movflags", "+faststart",
        str(output_path)
    ]
    print("正在转码:", input_path, "→", output_path)
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print("转码失败:", input_path, e)

def batch_convert(input_dir: str, output_dir: str):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in input_dir.rglob("*"):
        if file.suffix.lower() in VIDEO_EXTS:
            output_file = output_dir / (file.stem + ".mp4")
            convert_video(file, output_file)

if __name__ == "__main__":
    batch_convert(INPUT_DIR, OUTPUT_DIR)
    print("✅ 全部视频转码完成，结果保存在:", OUTPUT_DIR)
