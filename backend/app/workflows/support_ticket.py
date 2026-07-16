import time

from backend.app.tracing.tracer import WorkflowTracer
from backend.app.models.workflow import (
    TicketRequest,
    TicketClassification,
    WorkflowResponse,
)


class SupportTicketWorkflow:

    def classify_ticket(self, ticket: TicketRequest) -> TicketClassification:

        text = (ticket.subject + " " + ticket.description).lower()

        if "login" in text or "password" in text:
            return TicketClassification(
                category="Technical Support",
                confidence=0.95,
            )

        elif "payment" in text or "refund" in text:
            return TicketClassification(
                category="Billing",
                confidence=0.93,
            )

        else:
            return TicketClassification(
                category="General Inquiry",
                confidence=0.75,
            )

    def retrieve_context(self, classification: TicketClassification):

        return [
            "Knowledge Base Article 001",
            "Internal Support Guide",
        ]

    def generate_response(self, category: str):

        return f"Support response generated for {category}."

    def validate_response(self, response: str):

        return len(response) > 10

    def execute(self, ticket: TicketRequest):
        tracer = WorkflowTracer()
        start = time.time()

        classification = self.classify_ticket(ticket)

        end = time.time()

        tracer.record_span(
            "Classification",
            start,
            end,
            "completed"
        )
        start = time.time()

        context = self.retrieve_context(classification)

        end = time.time()

        tracer.record_span(
            "Retrieval",
            start,
            end,
            "completed"
        )
        start = time.time()

        response = self.generate_response(classification.category)

        end = time.time()

        tracer.record_span(
            "Generation",
            start,
            end,
            "completed"
        )
        start = time.time()

        is_valid = self.validate_response(response)

        end = time.time()

        tracer.record_span(
            "Validation",
            start,
            end,
            "completed"
        )

        status = "completed" if is_valid else "failed"
        trace = tracer.get_trace()
        print(trace.model_dump_json(indent=4))  
        return WorkflowResponse(
        ticket_id=ticket.ticket_id,
        trace_id=trace.trace_id,
        category=classification.category,
        confidence=classification.confidence,
        generated_response=response,
        status=status,
)