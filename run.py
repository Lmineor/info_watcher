import schedule
import time

from info_watcher.watcher import watcher
from info_watcher.logger.logger import logger


def job():
    watcher()
    logger.info("end watcher")


def start():
    logger.info("starting tasks...")
    job()  # 启动的时候run一次
    # 每天12点执行job函数
    # schedule.every().day.at("12:00").do(job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)


start()
