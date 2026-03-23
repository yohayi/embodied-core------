import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\THERMAL"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_thermal_data(data):
    """处理MLX90614红外测温数据"""
    thermal_data = data.get("mlx90614")
    if not thermal_data:
        return
    timestamp = data["timestamp"]
    date_str = timestamp.split(" ")[0]
    filename = os.path.join(BASE_DIR, f"{date_str}_mlx90614.csv")
    file_exists = os.path.isfile(filename)

    flat_data = {
        "timestamp": timestamp,
        "ambient_temp": thermal_data.get("ambient_temp"),
        "object_temp": thermal_data.get("object_temp")
    }

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(flat_data)
    print(f"[THERMAL] 保存红外测温数据: {flat_data}")