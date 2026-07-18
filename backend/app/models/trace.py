from pydantic import BaseModel
from typing import List, Any
from datetime import datetime


class Span(BaseModel):
    step: str
    status: str
    latency_ms: float
    timestamp: datetime
    input_data: Any = None
    output_data: Any = None
    error: str | None = None


class Trace(BaseModel):
    trace_id: str
    spans: List[Span]