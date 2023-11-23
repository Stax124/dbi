from fastapi import APIRouter
from fastapi.websockets import WebSocket
from starlette.websockets import WebSocketDisconnect

from api import websocket_manager
from api.websockets.data import Data

router = APIRouter()


@router.websocket("/master")
async def master_endpoint(websocket: WebSocket):
    "Main connection point for the websocket"

    await websocket_manager.connect(websocket)
    try:
        while True:
            text = await websocket.receive_text()
            if text == "ping":
                await websocket.send_text("pong")

    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)
