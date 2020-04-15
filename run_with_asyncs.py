import time
from typing import List
import asyncio

from Slog import logger
from config import INTERVAL, ZDH, XGS, WLXXZX, JSS, KYB
from spider import get_info_zdh, get_info_jss, get_info_xgs, get_info_wlxxzx, get_info_kyb
from send_email import send_email


logger.info("Start run.py")

zdh_old_info = []
jss_old_info = []
wlxxzx_old_info = []
xgs_old_info = []
kyb_old_info = []

time_buffer = 0


def asyncs(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

@asyncs
def run():
    global zdh_old_info
    global jss_old_info
    global wlxxzx_old_info
    global xgs_old_info
    global kyb_old_info
    
    
    try:
        zdh_new_info = get_info_zdh() # 自动化所最新消息
        wlxxzx_new_info = get_info_wlxxzx() # 网络信息中心最新消息
        xgs_new_info = get_info_xgs() # 信工所最新消息
        jss_new_info = get_info_jss() # 计算所最新消息
        # 第三方网站
        kyb_new_info = get_info_kyb() # 考研帮最新消息
    except Exception as e:
        logger.error(e)
    diff_total = []
    if diff(zdh_new_info, zdh_old_info):
        diff_total = diff_total + ['自动化所', ZDH] + diff(zdh_new_info, zdh_old_info) + ['']
    if diff(wlxxzx_new_info, wlxxzx_old_info):
        diff_total = diff_total + ['网络信息中心', WLXXZX] + diff(wlxxzx_new_info, wlxxzx_old_info) + ['']
    if diff(xgs_new_info, xgs_old_info):
        diff_total = diff_total + ['信工所', XGS] + diff(xgs_new_info, xgs_old_info) + ['']
    if diff(jss_new_info, jss_old_info):
        diff_total = diff_total + ['计算所', JSS] + diff(jss_new_info, jss_old_info) + ['']
    if diff(kyb_new_info, kyb_old_info):
        diff_total = diff_total + ['考研帮', KYB] + diff(kyb_new_info, kyb_old_info) + ['']
    if '\n'.join(diff_total):
        contend = '\n'.join(diff_total) # 邮件内容
        froms = '招生信息更新'
        to = '雒海艇'
        subject = "招生信息更新"
        send_email(contend, froms, to, subject)


    zdh_old_info = zdh_new_info
    wlxxzx_old_info = wlxxzx_new_info
    xgs_old_info = xgs_new_info
    jss_old_info = jss_new_info
    kyb_old_info = kyb_new_info
    time.sleep(INTERVAL)


def diff(new_info, old_info) -> list:
    if not old_info:
        return new_info
    else:
        return new_info[:new_info.index(old_info[0])]


async  def run2():
    print('正在运行\n')
    time.sleep(30)


async  def is_alive():
    print('还活着\n')
    time.sleep(60)
    # if time_buffer//


if __name__ == '__main__':
    for i in range(5):
        run2()
        is_alive()
    # while True:
    #     run2()
    #     is_alive()