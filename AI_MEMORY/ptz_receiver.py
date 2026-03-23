import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\PTZ"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_ptz_data(data):
    """处理PTZ双舵机云台数据"""
    ptz_data = data.get("ptz_camera")
    if not ptz_data:
        return
    timestamp = data["timestamp"]
    date_str = timestamp.split(" ")[0]
    filename = os.path.join(BASE_DIR, f"{date_str}_ptz.csv")
    file_exists = os.path.isfile(filename)

    flat_data = {
        "timestamp": timestamp,
        "pan_angle": ptz_data.get("pan_angle", 90),
        "tilt_angle": ptz_data.get("tilt_angle", 45)
    }

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(flat_data)
    print(f"[PTZ] 保存云台角度数据: {flat_data}")