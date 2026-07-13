import pandas as pd
import numpy as np

np.random.seed(42)

rows = 5000

cpu_usage = np.random.uniform(5, 100, rows)
memory_usage = np.random.uniform(10, 100, rows)
disk_usage = np.random.uniform(20, 98, rows)
network_sent = np.random.uniform(0, 1000, rows)
network_received = np.random.uniform(0, 1500, rows)
process_count = np.random.randint(50, 400, rows)
temperature = np.random.uniform(35, 95, rows)

risk_score = (
    0.35 * cpu_usage
    + 0.30 * memory_usage
    + 0.15 * disk_usage
    + 0.10 * temperature
    + 0.05 * process_count
    + 0.05 * (network_sent + network_received) / 20
)

risk_level = []

for score in risk_score:
    if score < 45:
        risk_level.append("Normal")
    elif score < 70:
        risk_level.append("Warning")
    else:
        risk_level.append("Critical")

df = pd.DataFrame({
    "cpu_usage": cpu_usage,
    "memory_usage": memory_usage,
    "disk_usage": disk_usage,
    "network_sent_mb": network_sent,
    "network_received_mb": network_received,
    "process_count": process_count,
    "temperature": temperature,
    "risk_level": risk_level
})

df.to_csv("data/system_metrics.csv", index=False)

print("Dataset generated successfully!")
print(df.head())