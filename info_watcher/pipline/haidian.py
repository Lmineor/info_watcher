#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json

from info_watcher.pipline.base import PipLineBase
from info_watcher.logger.logger import logger

"""
@Author  : lex(luohai2233@163.com)
"""


class HaiDian(PipLineBase):
    """
    监测`https://zyk.bjhd.gov.cn/jbdt/auto4522_51806/zdly/bzzf/`
    如果有新内容，则通知手机
    """
    filename = "haidian"
    url = "https://zyk.bjhd.gov.cn/jbdt/auto4522_51806/zdly/bzzf/"

    def bump(self, current_data):
        logger.info(f"into haidian pipline, before parse {current_data}")
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
            result.append(d['发文标题'] + '?url=' + self.url)
        return result


h = HaiDian()


def haidian_bump(current_data):
    return h.bump(current_data)
