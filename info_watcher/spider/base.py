#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import List

from bs4 import BeautifulSoup

from info_watcher.config import old_info_dir

"""
@Author  : lex(luohai2233@163.com)
"""


class Spider(object):
    filename = ""

    @staticmethod
    def drink_soup(page_source):
        soup = BeautifulSoup(page_source, 'html.parser')
        return soup

    def extract(self) -> List:
        raise NotImplementedError

    @staticmethod
    def read_old_info(filename):
        filename = os.path.join(old_info_dir, filename)
        with open(filename, 'r') as f:
            data = f.readlines()
        return data

    @staticmethod
    def write_new_info(filename, info):
        filename = os.path.join(old_info_dir, filename)
        with open(filename, 'w') as f:
            f.writelines(info)

    @staticmethod
    def compare_new_old(new_info, old_info):
        return diff(new_info, old_info)

    def run(self):
        new_infos = self.extract()
        old_infos = self.read_old_info(self.filename)
        diffs = self.compare_new_old(new_infos, old_infos)
        self.write_new_info(self.filename, new_infos)
        return diffs


def diff(new_info: List, old_info: List) -> List:
    diffs = []
    for item in new_info:
        if item not in old_info:
            diffs.append(item)
    return diffs
