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

    prompt: str | None = None

    model: str | None = None

    provider: str | None = None

    token_usage: int | None = None

    estimated_cost: float | None = None

    artifacts: list[Any] = []

    error: str | None = None


class Trace(BaseModel):

    trace_id: str

    spans: List[Span]