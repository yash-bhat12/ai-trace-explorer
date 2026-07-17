from backend.app.models.workflow import (
    TicketRequest,
    TicketClassification,
    WorkflowResponse,
)

from backend.app.tracing.tracer import WorkflowTracer
from backend.app.storage.trace_store import trace_store


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

        # Create a tracer for this workflow execution
        tracer = WorkflowTracer()

        # Wrap each workflow step with automatic tracing
        classification_step = tracer.trace_step("Classification")(self.classify_ticket)
        retrieval_step = tracer.trace_step("Retrieval")(self.retrieve_context)
        generation_step = tracer.trace_step("Generation")(self.generate_response)
        validation_step = tracer.trace_step("Validation")(self.validate_response)

        # Execute the workflow
        classification = classification_step(ticket)

        context = retrieval_step(classification)

        response = generation_step(classification.category)

        is_valid = validation_step(response)

        status = "completed" if is_valid else "failed"

        # Get the completed trace
        trace = tracer.get_trace()

        # Save the trace
        trace_store.save(trace)

        # Print the trace in the terminal (temporary for debugging)
        print(trace.model_dump_json(indent=4))

        return WorkflowResponse(
            ticket_id=ticket.ticket_id,
            trace_id=trace.trace_id,
            category=classification.category,
            confidence=classification.confidence,
            generated_response=response,
            status=status,
        )