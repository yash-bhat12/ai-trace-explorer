from fastapi import APIRouter

from backend.app.storage.trace_store import trace_store

router = APIRouter()


@router.get("/traces")
def list_traces():

    return trace_store.get_all()


@router.get("/traces/{trace_id}")
def get_trace(trace_id: str):

    return trace_store.get(trace_id)