import psutil
import requests
import time
import random

API_URL ="https://ai-system-monitoring.onrender.com/predict"

previous_network = psutil.net_io_counters()

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    current_network = psutil.net_io_counters()

    network_sent_mb = (
        current_network.bytes_sent - previous_network.bytes_sent
    ) / (1024 * 1024)

    network_received_mb = (
        current_network.bytes_recv - previous_network.bytes_recv
    ) / (1024 * 1024)

    previous_network = current_network

    process_count = len(psutil.pids())

    # Most laptops do not expose temperature sensors consistently.
    # This is a safe simulated value for the first version.
    temperature = random.uniform(40, 85)

    payload = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage,
        "network_sent_mb": round(network_sent_mb, 2),
        "network_received_mb": round(network_received_mb, 2),
        "process_count": process_count,
        "temperature": round(temperature, 2)
    }

    try:
        response = requests.post(API_URL, json=payload)
        print("Metrics:", payload)
        print("Prediction:", response.json())
    except Exception as error:
        print("API connection error:", error)

    time.sleep(5)