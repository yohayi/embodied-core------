import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\ANALOG"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_analog_data(data):
    """处理ADS1115 ADC、MQ2气体传感器数据"""
    timestamp = data["timestamp"]
    date_str = timestamp.split(" ")[0]
    sensors = ["ads1115", "mq2"]

    for sensor in sensors:
        sensor_data = data.get(sensor)
        if not sensor_data:
            continue
        filename = os.path.join(BASE_DIR, f"{date_str}_{sensor}.csv")
        file_exists = os.path.isfile(filename)

        flat_data = {"timestamp": timestamp}
        if isinstance(sensor_data, list):
            for i, v in enumerate(sensor_data):
                flat_data[f"{sensor}_{i}"] = v
        elif isinstance(sensor_data, dict):
            flat_data.update(sensor_data)
        else:
            flat_data[sensor] = sensor_data

        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=flat_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(flat_data)
        print(f"[ANALOG] 保存{sensor}数据: {flat_data}")