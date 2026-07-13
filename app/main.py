from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
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
    metrics = db.query(SystemMetric).order_by(
        SystemMetric.created_at.desc()
    ).limit(100).all()

    return metrics