from sqlalchemy import Column, Integer, Float, DateTime, String
from datetime import datetime
from app.database import Base

class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, index=True)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(Float)
    network_sent_mb = Column(Float)
    network_received_mb = Column(Float)
    process_count = Column(Integer)
    temperature = Column(Float)
    predicted_risk = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)