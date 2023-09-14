import asyncio
import logging
from asyncio import AbstractEventLoop
from typing import List, Optional

from fastapi import WebSocket

from api.websockets.data import Data

logger = logging.getLogger(__name__)


class WebSocketManager:
    "Manages active websocket connections"

    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.loop: Optional[AbstractEventLoop] = None

    async def connect(self, websocket: WebSocket):
        "Accepts a new websocket connection and adds it to the list of active connections"

        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        "Removes a websocket connection from the list of active connections"

        self.active_connections.remove(websocket)

    async def send_personal_message(self, data: Data, websocket: WebSocket):
        "Sends a data message to a specific websocket connection"

        await websocket.send_json(data.to_json())

    async def broadcast(self, data: Data):
        "Broadcasts data message to all active websocket connections"

        for connection in self.active_connections:
            if connection.application_state.CONNECTED:
                try:
                    await connection.send_json(data.to_json())
                except RuntimeError:
                    logger.debug("RuntimeError, removing connection")
                    await connection.close()
                    self.active_connections.remove(connection)
            else:
                self.active_connections.remove(connection)

    def broadcast_sync(self, data: Data):
        "Broadcasts data message to all active websocket connections synchronously"

        loop_error_message = "No event loop found, please inject it in the code"

        try:
            assert self.loop is not None, loop_error_message
            asyncio.get_event_loop()
        except RuntimeError:
            assert self.loop is not None  # For type safety
            asyncio.set_event_loop(self.loop)
        except AssertionError:
            logger.info("WARNING: No event loop found, assuming we are running tests")
            return

        for connection in self.active_connections:
            if connection.application_state.CONNECTED:
                asyncio.run_coroutine_threadsafe(
                    connection.send_json(data.to_json()), self.loop
                )
            else:
                self.active_connections.remove(connection)

    async def close_all(self):
        "Closes all active websocket connections"

        for connection in self.active_connections:
            await connection.close(reason="Server shutdown")

        self.active_connections = []
