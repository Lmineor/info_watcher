#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author  : lex(luohai2233@163.com)
"""
import os
import time

import requests

from info_watcher.logger.logger import logger

BARK_KEY = os.environ.get('BARK_KEY')
BARK_PORT = os.environ.get('BARK_PORT')


class Msg(object):
    """
    Msg 代表通知给手机的一条信息
    """

    def __init__(self, title, content):
        self.title = title
        self.content = content


class Bark(object):

    def __init__(self, code_map):
        self.msg_loop = []
        self.code_map = code_map

    def notify_app(self, msgs):
        for key, items in msgs.items():
            logger.info(f"msg key {key}, contents {items}")
            for item in items:
                self.msg_loop.append(Msg(self.code_map[key], item))

        self.notify()

    def notify(self):
        for msg in self.msg_loop:
            time.sleep(1)
            self._notify(msg)

    @staticmethod
    def _notify(msg):
        try:
            logger.info(f"send msg to app, title is {msg.title}, content is {msg.content}")
            requests.get(f"http://112.126.23.119:{BARK_PORT}/{BARK_KEY}/{msg.title}/{msg.content}")
        except Exception as e:
            logger.error(f"failed to notify app, {e}")
