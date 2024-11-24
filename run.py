import schedule
import time

from info_watcher.watcher import watcher
from info_watcher.logger.logger import logger


def job(run_on_start=False):
    watcher(run_on_start)
    logger.info("end watcher")


def start():
    logger.info("starting tasks...")
    job(run_on_start=True)  # 启动的时候run一次
    # 每天12点执行job函数
    schedule.every().day.at("12:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


start()
