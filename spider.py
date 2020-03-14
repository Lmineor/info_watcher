# coding = utf-8
import re
from typing import List

import requests
from bs4 import BeautifulSoup

from config import ZDH, JSS, XGS, WLXXZX, KYB, SXS
from send_email import send_email
from Slog import logger

def get_info_zdh() -> list:
    # 自动化所信息
    logger.info("开始查询自动化所招生信息")
    rep = get_req(ZDH)
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
    rep = get_req(JSS)
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
    rep = get_req(XGS)
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
    rep = get_req(WLXXZX)
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
    rep = get_req(KYB)
    soup = BeautifulSoup(rep.text, 'html.parser')
    li_list = soup.find('ul', attrs={'class':'list areaZslist'})
    re_pattern = '(?<=>).+?(?=<)'
    res = []
    for li in li_list:
        title = re.findall(re_pattern, str(li.find('a')))
        if title:
            res.append(title[0])
    return res

def get_info_sxs() -> list:
    # 自动化所信息
    logger.info("开始查询声学所所招生信息")
    req = get_req(SXS)
    soup = BeautifulSoup(rep.text, 'html.parser')
    trs = soup.find_all('table')

    table_info = soup.select('body>table:nth-of-type(6)>tbody>tr>td:nth-of-type(3)>table:nth-of-type(2)>tbody>tr>td>table:nth-of-type(3)>tbody>tr')
    print(table_info)
    'body > table:nth-child(6) > tbody > tr > td:nth-child(3) > table:nth-child(2) > tbody > tr > td > table:nth-child(3) > tbody > tr:nth-child(1)'
    # re_pattern = '(?<=>).+?(?=<)'
    # 'body > table:nth-child(6) > tbody > tr > td:nth-child(3) > table:nth-child(2) > tbody > tr > td > table:nth-child(3)'
    # res = []
    # for li in li_list:
    #     title = re.findall(re_pattern, str(li.find('a')))
    #     if title:
    #         res.append(title[0])
    # return res


def get_req(url):
    rep = requests.get(KYB, timeout=5)
    rep.encoding = 'utf-8'
    return rep

if __name__ == '__main__':
    print(get_info_kyb())