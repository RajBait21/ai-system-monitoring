import joblib
import numpy as np

model = joblib.load("ml/system_risk_model.pkl")
label_encoder = joblib.load("ml/label_encoder.pkl")

def predict_system_risk(metrics):
    values = np.array([[
        metrics.cpu_usage,
        metrics.memory_usage,
        metrics.disk_usage,
        metrics.network_sent_mb,
        metrics.network_received_mb,
        metrics.process_count,
        metrics.temperature
    ]])

    prediction = model.predict(values)[0]
    probabilities = model.predict_proba(values)[0]

    risk_level = label_encoder.inverse_transform([prediction])[0]
    confidence = float(max(probabilities))

    return risk_level, confidence