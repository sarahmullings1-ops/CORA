# api/routes/webhooks.py
from fastapi import APIRouter

router = APIRouter(prefix="/webhook", tags=["webhooks"])

@router.post("/missed-call")
async def missed_call():
    return {"received": True}

@router.post("/sms")
async def inbound_sms():
    return {"received": True}