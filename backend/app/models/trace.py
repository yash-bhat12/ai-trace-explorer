from pydantic import BaseModel
from typing import List


class Span(BaseModel):
    step: str
    status: str
    latency_ms: float


class Trace(BaseModel):
    trace_id: str
    spans: List[Span]