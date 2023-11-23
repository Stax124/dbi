import argparse
import asyncio
import logging
import sys

from rich.logging import RichHandler
from uvicorn import run

from api.app import app

parser = argparse.ArgumentParser(description="Start the API")
parser.add_argument(
    "--host", action="store_true", help="Allow connections from any host"
)
parser.add_argument("--port", type=int, default=8080, help="Port to listen on")
parser.add_argument(
    "--log-level",
    type=str,
    default="INFO",
    help="Log level to use (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
)

args = parser.parse_args()

# Inject better logger
from rich.logging import RichHandler

logging.basicConfig(
    level=args.log_level,
    format="%(asctime)s | %(name)s » %(message)s",
    datefmt="%H:%M:%S",
    handlers=[RichHandler(rich_tracebacks=True, show_time=False)],
)
logger = logging.getLogger()


def main():
    # Start the API
    from uvicorn import Config, Server

    from api.app import app as api_app

    host = "0.0.0.0" if args.host else "127.0.0.1"

    uvi_config = Config(app=api_app, host=host, port=args.port)
    uvi_server = Server(config=uvi_config)

    uvi_config.setup_event_loop()

    try:
        asyncio.run(uvi_server.serve())
    except RuntimeError:
        logger.info("Server stopped")
        sys.exit(0)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
