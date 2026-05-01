# File: sensor_logger.py
# Simple Raspberry Pi GPIO + CSV logger project for today's GitHub commit

import time
import csv
from datetime import datetime
import random

LOG_FILE = "temperature_log.csv"

def read_fake_temperature():
    # Simulated sensor value (replace with real sensor later)
    return round(random.uniform(24.0, 32.0), 2)

def log_data():
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        while True:
            temp = read_fake_temperature()
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([now, temp])
            file.flush()

            print(f"Logged: {now} | Temp: {temp} °C")
            time.sleep(5)

if __name__ == "__main__":
    try:
        log_data()
    except KeyboardInterrupt:
        print("Logging stopped.")
