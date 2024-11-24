import logging

from info_watcher.config import LOG_FILE

_g_logger = None


def _get_logger():
    global _g_logger
    if _g_logger is None:
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
        __datetime = "%Y-%m-%d %H:%M:%S"
        __format_str = "%(asctime)s %(levelname).1s [%(filename)s:%(lineno)s] %(message)s"
        _g_logger = logging.getLogger()
        # stream header
        formater = logging.Formatter(__format_str, __datetime)
        handler = logging.StreamHandler()
        handler.setFormatter(formater)
        _g_logger.addHandler(handler)
    return _g_logger


logger = _get_logger()
