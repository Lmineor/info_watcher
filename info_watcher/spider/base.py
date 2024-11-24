#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from info_watcher.config import OLD_INFO_DIR

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
        filename = os.path.join(OLD_INFO_DIR, filename)
        with open(filename, 'r') as f:
            data = f.readlines()
        return data

    @staticmethod
    def write_new_info(filename, info):
        filename = os.path.join(OLD_INFO_DIR, filename)
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

    def get_soup(self, url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无头模式运行，不需要图形界面
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片，提升速度
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
        return self.drink_soup(page_source)


def diff(new_info: List, old_info: List) -> List:
    diffs = []
    for item in new_info:
        if item not in old_info:
            diffs.append(item)
    return diffs
