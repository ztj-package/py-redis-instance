# -*- coding: utf-8 -*-
# Intro: Redis 模块
# Author: Ztj
# Email: ztj1993@gmail.com

import os
import time

import redis


class Redis(object):

    def __init__(self, **kwargs):
        self.pool = None
        self.server = None
        self.options = {
            **dict(
                host=os.environ.get('REDIS_HOST', '127.0.0.1'),
                port=int(os.environ.get('REDIS_PORT', 6379)),
                db=int(os.environ.get('REDIS_DB', 0)),
                password=os.environ.get('REDIS_PASSWORD', None),
                decode_responses=True,
            ),
            **kwargs,
        }

    def option(self, key, value):
        self.options[key] = value

    def destroy(self):
        self.pool = None
        self.server = None

    def connect(self) -> redis.Redis:
        if self.server is None:
            self.pool = redis.ConnectionPool(**self.options)
            self.server = redis.Redis(connection_pool=self.pool)
        return self.server

    def ping(self):
        try:
            self.connect().ping()
            return True
        except:
            return False

    def wait(self, interval_time=60):
        while self.ping() is False:
            time.sleep(interval_time)
