import logging
import mimetypes

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.responses import JSONResponse

from api import websocket_manager
from api.database import create_default_user, create_metadata
from api.routes import static, test, users, ws
from api.websockets.notification import Notification

logger = logging.getLogger(__name__)

create_metadata()
create_default_user()


async def log_request(request: Request):
    "Log all requests"

    logger.debug(
        f"url: {request.url}"
        # f"url: {request.url}, params: {request.query_params}, body: {await request.body()}"
    )


app = FastAPI(
    docs_url="/api/docs", redoc_url="/api/redoc", dependencies=[Depends(log_request)]
)

mimetypes.init()
mimetypes.add_type("application/javascript", ".js")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request: Request, exc: RequestValidationError):
    "Output validation errors into debug log for debugging purposes"

    logger.debug(exc)

    try:
        why = str(exc).split(":")[1].strip()
        await websocket_manager.broadcast(
            data=Notification(
                severity="error",
                message=f"Validation error: {why}",
                title="Validation Error",
            )
        )
    except IndexError:
        logger.debug("Unable to parse validation error, skipping the error broadcast")

    content = {
        "status_code": 10422,
        "message": f"{exc}".replace("\n", " ").replace("   ", " "),
        "data": None,
    }
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


@app.exception_handler(404)
async def custom_http_exception_handler(_request, _exc):
    "Redirect back to the main page (frontend will handle it)"

    return FileResponse("frontend/dist/index.html")


@app.on_event("startup")
async def startup_event():
    "Prepare the event loop for other asynchronous tasks"

    # Inject the logger
    from rich.logging import RichHandler

    # Disable duplicate logger
    logging.getLogger("uvicorn").handlers = []

    for logger_ in ("uvicorn.access", "uvicorn.error", "fastapi"):
        log = logging.getLogger(logger_)
        handler = RichHandler(
            rich_tracebacks=True, show_time=False, omit_repeated_times=False
        )
        handler.setFormatter(
            logging.Formatter(
                fmt="%(asctime)s | %(name)s » %(message)s", datefmt="%H:%M:%S"
            )
        )
        log.handlers = [handler]

    logger.info("Started WebSocketManager performance monitoring loop")
    logger.info("UI Available at: http://localhost:8080/")


@app.on_event("shutdown")
async def shutdown_event():
    "Close all WebSocket connections"

    logger.info("Closing all WebSocket connections")
    await websocket_manager.close_all()


# Mount routers
## HTTP
app.include_router(static.router)
app.include_router(test.router, prefix="/api/test")
app.include_router(users.router, prefix="/api/users")

## WebSockets
app.include_router(ws.router, prefix="/api/websockets")

# Static files
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"), name="assets")

# Allow CORS for specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
