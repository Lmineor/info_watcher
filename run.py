import time
from typing import List
import asyncio

from Slog import logger
from config import INTERVAL
from spider import get_info_from_schools
from send_email import send_email


logger.info("Start run.py")

schoo_old_news = []
def run():
    global schoo_old_news
    try:
        schoo_new_news = get_info_from_schools()
    except Exception as e:
        logger.error(e)
        schoo_new_news = ['']
    if diff(schoo_new_news, schoo_old_news):
        _diff = diff(schoo_new_news, schoo_old_news)
    if '\n'.join(_diff):
        contend = '\n'.join(_diff) # 邮件内容
        froms = '招生信息更新'
        to = '雒海艇'
        subject = "招生信息更新"
        send_email(contend, froms, to, subject)
    schoo_old_news = schoo_new_news


def diff(new_info, old_info) -> list:
    if not old_info:
        return new_info
    else:
        return new_info[:new_info.index(old_info[0])]


if __name__ == '__main__':
    while True:
        run()
        time.sleep(INTERVAL)