#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import List

from info_watcher.spider.base import Spider
from info_watcher.logger.logger import logger

"""
@Author  : lex(luohai2233@163.com)
"""


class YouZhengSpider(Spider):
    """
    监测`https://mall.11185.cn/web/searchJy?businessId=JY&prodGoodsType=NORMAL&classficationId=JY-0`
    如果有新内容，则通知手机
    """
    url = "https://mall.11185.cn/web/searchJy?businessId=JY&prodGoodsType=NORMAL&classficationId=JY-0"
    filename = "youzheng"

    def extract(self) -> List:
        results = []
        logger.info("开始检测{}".format(self.url))
        soup = self.get_soup(self.url)
        detail_body = soup.find('div', class_='detail_center')
        card_con1s = detail_body.find_all('div', class_='card_con1')
        for card_con1 in card_con1s:
            if card_con1:
                results.append(card_con1.get_text(strip=True))

        return results
