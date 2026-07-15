from fastapi import APIRouter

from backend.app.models.workflow import (
    TicketRequest,
    WorkflowResponse,
)

from backend.app.workflows.support_ticket import SupportTicketWorkflow

router = APIRouter()

workflow = SupportTicketWorkflow()


@router.post("/workflow/run", response_model=WorkflowResponse)
def run_workflow(ticket: TicketRequest):

    result = workflow.execute(ticket)

    return result