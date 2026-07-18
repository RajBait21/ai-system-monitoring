from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import psutil
import random

from app.alert_service import send_alert
from app.database import Base, engine, get_db
from app.models import SystemMetric
from app.schemas import MetricInput, PredictionResponse
from app.predictor import predict_system_risk

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Real-Time System Monitoring API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Real-Time System Monitoring API is running"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(metrics: MetricInput, db: Session = Depends(get_db)):
    risk_level, confidence = predict_system_risk(metrics)

    send_alert(risk_level, confidence)

    new_metric = SystemMetric(
        cpu_usage=metrics.cpu_usage,
        memory_usage=metrics.memory_usage,
        disk_usage=metrics.disk_usage,
        network_sent_mb=metrics.network_sent_mb,
        network_received_mb=metrics.network_received_mb,
        process_count=metrics.process_count,
        temperature=metrics.temperature,
        predicted_risk=risk_level
    )

    db.add(new_metric)
    db.commit()
    db.refresh(new_metric)

    return {
        "risk_level": risk_level,
        "confidence": round(confidence, 4)
    }


@app.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):

    # Collect live system metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    net = psutil.net_io_counters()
    network_sent = round(net.bytes_sent / (1024 * 1024), 2)
    network_received = round(net.bytes_recv / (1024 * 1024), 2)

    process_count = len(psutil.pids())

    # Temperature (random if sensors unavailable)
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            first_sensor = list(temps.values())[0]
            temperature = first_sensor[0].current
        else:
            temperature = random.uniform(40, 80)
    except Exception:
        temperature = random.uniform(40, 80)

    # Predict risk
    metric_input = MetricInput(
        cpu_usage=cpu,
        memory_usage=memory,
        disk_usage=disk,
        network_sent_mb=network_sent,
        network_received_mb=network_received,
        process_count=process_count,
        temperature=temperature
    )

    risk_level, confidence = predict_system_risk(metric_input)

    # Save latest metrics
    new_metric = SystemMetric(
        cpu_usage=cpu,
        memory_usage=memory,
        disk_usage=disk,
        network_sent_mb=network_sent,
        network_received_mb=network_received,
        process_count=process_count,
        temperature=temperature,
        predicted_risk=risk_level
    )

    db.add(new_metric)
    db.commit()

    # Return latest 100 records
    metrics = (
        db.query(SystemMetric)
        .order_by(SystemMetric.created_at.desc())
        .limit(100)
        .all()
    )

    return metrics