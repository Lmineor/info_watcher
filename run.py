from info_watcher.server import app
from info_watcher.logger.logger import logger


def start():
    logger.info("starting tasks...")
    app.run(debug=False, host="0.0.0.0", port=9999)


start()