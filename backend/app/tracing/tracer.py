print("Loaded tracer.py")
import uuid
import time
from functools import wraps

from backend.app.models.trace import Trace, Span


class WorkflowTracer:

    def __init__(self):

        self.trace = Trace(
            trace_id=str(uuid.uuid4()),
            spans=[]
        )

    def trace_step(self, step_name):

        def decorator(func):

            @wraps(func)
            def wrapper(*args, **kwargs):

                start = time.time()

                status = "completed"

                try:
                    result = func(*args, **kwargs)

                except Exception:

                    status = "failed"

                    raise

                finally:

                    end = time.time()

                    latency = (end - start) * 1000

                    self.trace.spans.append(
                        Span(
                            step=step_name,
                            status=status,
                            latency_ms=round(latency, 2)
                        )
                    )

                return result

            return wrapper

        return decorator

    def get_trace(self):
        return self.trace