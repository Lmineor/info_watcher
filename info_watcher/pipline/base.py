#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import List

from info_watcher.logger.logger import logger
from info_watcher.config import STORE

"""
@Author  : lex(luohai2233@163.com)
"""


class PipLineBase(object):
    filename = ""

    @staticmethod
    def read_previous_data(filename):
        if filename == "":
            raise Exception("filename empty")
        infos = []
        filename = os.path.join(STORE, filename)
        try:
            with open(filename, 'r') as f:
                for line in f:
                    infos.append(line.strip())
        except FileNotFoundError:
            pass
        return infos

    @staticmethod
    def write_new_info(filename, info):
        if filename == "":
            raise Exception("filename empty")
        filename = os.path.join(STORE, filename)
        with open(filename, 'w') as f:
            for item in info:
                # 将每个元素写入文件，并在每个元素后添加换行符
                f.write(item + '\n')

    @staticmethod
    def compare_new_old(new_info, old_info):
        return diff(new_info, old_info)

    def _parse(self, current_data):
        previous_data = self.read_previous_data(self.filename)
        diffs = self.compare_new_old(current_data, previous_data)
        self.write_new_info(self.filename, current_data)
        return diffs

    def bump(self, current_data):
        logger.info(f"current data is {current_data}")
        diffs = self._parse(current_data)
        return diffs


def diff(new_info: List, old_info: List) -> List:
    diffs = []
    if len(old_info) == 0:
        return []
    for item in new_info:
        if item not in old_info:
            diffs.append(item)
    return diffs
