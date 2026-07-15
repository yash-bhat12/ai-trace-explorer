from pydantic import BaseModel


class TicketRequest(BaseModel):
    ticket_id: int
    customer_name: str
    subject: str
    description: str


class TicketClassification(BaseModel):
    category: str
    confidence: float


class WorkflowResponse(BaseModel):
    ticket_id: int
    category: str
    confidence: float
    generated_response: str
    status: str