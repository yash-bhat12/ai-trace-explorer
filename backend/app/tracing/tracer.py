import uuid
import time
from functools import wraps
from datetime import datetime

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

                result = None

                error = None

                try:

                    result = func(*args, **kwargs)

                    return result

                except Exception as e:

                    status = "failed"

                    error = str(e)

                    raise

                finally:

                    end = time.time()

                    latency = round((end - start) * 1000, 2)

                    self.trace.spans.append(

                        Span(
                            step=step_name,
                            status=status,
                            latency_ms=latency,
                            timestamp=datetime.now(),
                            input_data=str(args),
                            output_data=str(result),
                            error=error
                        )

                    )

            return wrapper

        return decorator

    def get_trace(self):

        return self.trace