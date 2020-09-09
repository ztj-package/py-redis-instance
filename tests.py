# -*- coding: utf-8 -*-
# Intro: Redis 模块单元测试
# Author: Ztj
# Email: ztj1993@gmail.com

import unittest

from ZtjRedis import Redis


class TestRedis(unittest.TestCase):

    def test_ping(self):
        """测试联通"""
        redis = Redis()
        self.assertTrue(redis.ping())


if __name__ == '__main__':
    unittest.main()
