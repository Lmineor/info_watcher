#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author  : lex(luohai2233@163.com)
"""

from info_watcher.spider.Youzheng import YouZhengSpider
from info_watcher.bark.messages import Bark
from info_watcher.logger.logger import logger


def watcher(run_on_start=False):
    logger.info("trigger task")
    messages = {}
    code_map = {"youzheng": "邮政"}

    messages['youzheng'] = YouZhengSpider().run()
    if not run_on_start:
        b = Bark(code_map)
        b.notify_app(messages)
    return messages
