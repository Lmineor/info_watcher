# coding = utf-8
import re
from typing import List

import requests
from bs4 import BeautifulSoup

from config import ZDH, JSS, XGS, WLXXZX, KYB
from send_email import send_email
from Slog import logger

def get_info_zdh() -> list:
    # 自动化所信息
    logger.info("开始查询自动化所招生信息")
    rep = requests.get(ZDH)
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, 'html.parser')
    li_list = soup.find('ul', attrs={'class':'fontlist'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res

def get_info_jss() -> list:
    # 计算所信息
    logger.info("开始查询计算所招生信息")
    rep = requests.get(JSS)
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, 'html.parser')
    li_list = soup.findAll('td', attrs={'class':'black_14'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res



def get_info_xgs() -> list:
    # 信工所信息
    logger.info("开始查询信工所招生信息")
    rep = requests.get(JSS)
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, 'html.parser')
    li_list = soup.findAll('td', attrs={'class':'black_14'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res

def get_info_wlxxzx() -> list:
    # 网络信息中心信息
    logger.info("开始查询网络信息中心招生信息")
    rep = requests.get(WLXXZX)
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, 'html.parser')
    li_list = soup.find('ul', attrs={'class':'list-font margin-top-10 clearfix'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res


def get_info_kyb() -> list:
    # 考研帮信息查询
    logger.info("开始查询考研帮招生信息")
    rep = requests.get(KYB)
    rep.encoding = 'utf-8'
    soup = BeautifulSoup(rep.text, 'html.parser')
    li_list = soup.find('ul', attrs={'class':'list areaZslist'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res


if __name__ == '__main__':
    print(get_info_kyb())