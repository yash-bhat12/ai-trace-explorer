from fastapi import APIRouter

from backend.app.api.routes.health import router as health_router
from backend.app.api.routes.workflow import router as workflow_router
from backend.app.api.routes.traces import router as traces_router
router = APIRouter()

router.include_router(health_router)
router.include_router(workflow_router)
router.include_router(traces_router)