#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

from info_watcher.pipline.base import PipLineBase
from info_watcher.logger.logger import logger

"""
@Author  : lex(luohai2233@163.com)
"""


class YouZheng(PipLineBase):
    """
    监测`https://mall.11185.cn/web/searchJy?businessId=JY&prodGoodsType=NORMAL&classficationId=JY-0`
    如果有新内容，则通知手机
    """
    filename = "youzheng"

    def bump(self, current_data):
        logger.info(f"into youzheng pipline, before parse {current_data}")
        result = self._parse_origin_data(current_data)
        diffs = super().bump(result)
        return diffs

    def _parse_origin_data(self, data):
        if isinstance(data, str):
            try:
                # 尝试将字符串解析为 JSON
                data = json.loads(data)
            except json.JSONDecodeError:
                print("Invalid JSON string")
                return []

        result = []
        for d in data:
            result.append(d['value'])
        return result


c = YouZheng()


def bump(current_data):
    return c.bump(current_data)
