import json
import csv
import os
from datetime import datetime

BASE_DIR = r"D:\AI_MEMORY\ACTUATOR"
os.makedirs(BASE_DIR, exist_ok=True)

def handle_actuator_data(command_response):
    """处理继电器、舵机等执行器的指令响应"""
    if not command_response:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = timestamp.split(" ")[0]
    filename = os.path.join(BASE_DIR, f"{date_str}_actuator.csv")
    file_exists = os.path.isfile(filename)

    flat_data = {
        "timestamp": timestamp,
        "command": command_response.get("command", ""),
        "status": command_response.get("status", ""),
        "data": json.dumps(command_response.get("data", {}))
    }

    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=flat_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(flat_data)
    print(f"[ACTUATOR] 保存执行器响应: {flat_data}")