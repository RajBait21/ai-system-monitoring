from pydantic import BaseModel

class MetricInput(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_sent_mb: float
    network_received_mb: float
    process_count: int
    temperature: float

class PredictionResponse(BaseModel):
    risk_level: str
    confidence: float