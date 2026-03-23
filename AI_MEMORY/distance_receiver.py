import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\DISTANCE"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_distance_data(data):
    """处理VL53L0X激光、HC-SR04超声波测距数据"""
    timestamp = data["timestamp"]
    date_str = timestamp.split(" ")[0]
    sensors = ["vl53l0x", "hc_sr04"]

    for sensor in sensors:
        sensor_data = data.get(sensor)
        if sensor_data is None:
            continue
        filename = os.path.join(BASE_DIR, f"{date_str}_{sensor}.csv")
        file_exists = os.path.isfile(filename)

        flat_data = {
            "timestamp": timestamp,
            sensor: sensor_data
        }

        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=flat_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(flat_data)
        print(f"[DISTANCE] 保存{sensor}数据: {flat_data}")