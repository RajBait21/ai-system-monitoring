def send_alert(risk_level, confidence):
    if risk_level == "Critical":
        print(
            f"ALERT: Critical system risk detected. "
            f"Confidence: {confidence * 100:.2f}%"
        )