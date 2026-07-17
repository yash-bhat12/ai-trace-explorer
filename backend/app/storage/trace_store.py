from backend.app.models.trace import Trace


class TraceStore:

    def __init__(self):
        self.traces = {}

    def save(self, trace: Trace):
        self.traces[trace.trace_id] = trace

    def get(self, trace_id: str):
        return self.traces.get(trace_id)

    def get_all(self):
        return list(self.traces.values())


trace_store = TraceStore()