import uuid
import time

from backend.app.models.trace import Trace, Span


class WorkflowTracer:

    def __init__(self):

        self.trace = Trace(
            trace_id=str(uuid.uuid4()),
            spans=[]
        )

    def record_span(self, step_name, start_time, end_time, status):

        latency = (end_time - start_time) * 1000

        self.trace.spans.append(
            Span(
                step=step_name,
                status=status,
                latency_ms=round(latency, 2)
            )
        )

    def get_trace(self):

        return self.trace