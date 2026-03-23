import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\COLOR"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_color_data(data):
    """处理TCS34725颜色识别数据"""
    color_data = data.get("tcs34725")
    if not color_data:
        return
    timestamp = data["timestamp"]
    date_str = timestamp.split(" ")[0]
    filename = os.path.join(BASE_DIR, f"{date_str}_tcs34725.csv")
    file_exists = os.path.isfile(filename)

    flat_data = {
        "timestamp": timestamp,
        "red": color_data.get("red"),
        "green": color_data.get("green"),
        "blue": color_data.get("blue"),
        "color_temp": color_data.get("color_temp")
    }

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(flat_data)
    print(f"[COLOR] 保存颜色数据: {flat_data}")