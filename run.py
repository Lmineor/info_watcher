import time
from typing import List

from Slog import logger
from config import INTERVAL, ZDH, XGS, WLXXZX, JSS
from spider import get_info_zdh, get_info_jss, get_info_xgs, get_info_wlxxzx
from send_email import send_email


logger.info("Start run.py")

zdh_old_info = []
jss_old_info = []
wlxxzx_old_info = []
xgs_old_info = []



def run():
    global zdh_old_info
    global jss_old_info
    global wlxxzx_old_info
    global xgs_old_info

    zdh_new_info = get_info_zdh() # 自动化所最新消息
    wlxxzx_new_info = get_info_wlxxzx() # 网络信息中心最新消息
    xgs_new_info = get_info_xgs() # 信工所最新消息
    jss_new_info = get_info_jss() # 计算所最新消息

    diff_info = ['自动化所', ZDH, ''] + diff(zdh_new_info, zdh_old_info)
    diff_info = diff_info + ['网络信息中心', WLXXZX, ''] + diff(wlxxzx_new_info, wlxxzx_old_info)
    diff_info = diff_info + ['信工所', XGS, ''] + diff(xgs_new_info, xgs_old_info)
    diff_info = diff_info + ['计算所', JSS, ''] + diff(jss_new_info, jss_old_info)

    contend = '\n'.join(diff_info) # 邮件内容
    froms = '招生信息更新'
    to = '雒海艇'
    subject = "招生信息更新"
    send_email(contend, froms, to, subject)
    zdh_old_info = zdh_new_info
    wlxxzx_old_info = wlxxzx_new_info
    xgs_old_info = xgs_new_info
    jss_old_info = jss_new_info


def diff(new_info, old_info) -> list:
    return list(set(new_info)^set(old_info))


if __name__ == '__main__':
    while True:
        run()
        time.sleep(INTERVAL)