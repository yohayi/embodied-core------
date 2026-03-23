import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\DHT22ws"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_dht22_data(data):
    """处理DHT22温湿度数据"""
    if not data.get("dht22"):
        return
    timestamp = data["timestamp"]
    dht22_data = data["dht22"]
    date_str = timestamp.split(" ")[0]
    filename = os.path.join(BASE_DIR, f"{date_str}_dht22.csv")
    file_exists = os.path.isfile(filename)

    flat_data = {
        "timestamp": timestamp,
        "temperature": dht22_data.get("temperature"),
        "humidity": dht22_data.get("humidity")
    }

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(flat_data)
    print(f"[DHT22] 保存温湿度数据: {flat_data}")