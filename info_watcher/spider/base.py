#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from typing import List

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from info_watcher.logger.logger import logger
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

    # def get_soup(self, url):
    #     # set xvfb display since there is no GUI in docker container.
    #     # display = Display(visible=False, size=(800, 600))
    #     # display.start()
    #
    #     chrome_options = Options()
    #     chrome_options.binary_location = "chromedriver"
    #     chrome_options.add_argument("--no-sandbox")
    #     chrome_options.add_argument('--window-size=1420,1080')
    #     chrome_options.add_argument('--headless')  # 无头模式运行，不需要图形界面
    #     chrome_options.add_argument('--disable-gpu')  # 禁用GPU加速
    #     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    #     driver.get(url)
    #     page_source = driver.page_source
    #     driver.quit()
    #     return self.drink_soup(page_source)

    def get_soup(self, url):
        logger.info(f'connecting to {url} ...')
        time.sleep(5)
        options = webdriver.ChromeOptions()

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

        driver.get(url)
        page_source = driver.page_source
        driver.close()

        return self.drink_soup(page_source)


def diff(new_info: List, old_info: List) -> List:
    diffs = []
    for item in new_info:
        if item not in old_info:
            diffs.append(item)
    return diffs
