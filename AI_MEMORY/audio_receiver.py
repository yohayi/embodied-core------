import json
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\AUDIO_RAW"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_audio_data(data):
    """处理USB麦克风音频数据（这里先记录元数据，实际音频文件后续处理）"""
    audio_data = data.get("audio")
    if not audio_data:
        return
    timestamp = data["timestamp"].replace(":", "-")  # 文件名不能用冒号
    filename = os.path.join(BASE_DIR, f"{timestamp}_audio_meta.json")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(audio_data, f, indent=2, ensure_ascii=False)
    print(f"[AUDIO] 保存音频元数据: {filename}")