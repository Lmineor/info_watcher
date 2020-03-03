import time
from typing import List

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


def diff(new_info, old_info) -> list:
    if not old_info:
        return new_info
    else:
        return new_info[:new_info.index(old_info[0])]


if __name__ == '__main__':
    while True:
        run()
        time.sleep(INTERVAL)