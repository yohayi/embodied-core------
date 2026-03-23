import json
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\SYSTEM"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_system_status(status_data):
    """处理设备在线状态、系统信息"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(BASE_DIR, f"{timestamp}_system_status.json")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(status_data, f, indent=2, ensure_ascii=False)
    print(f"[SYSTEM] 保存系统状态: {filename}")