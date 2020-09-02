# -*- coding=utf-8 -*-
# Copyright (C) 2016-2020 ActionTech.
# License: https://www.mozilla.org/en-US/MPL/2.0 MPL version 2 or higher.
# @Time    : 2020/4/3 AM11:18
# @Author  : irene-coming

class Parent(object):
    def __init__(self, config_dic):
        """
        test inherit of child
        """
        self._config_dic = config_dic.copy()
        print("config dic in parent:", config_dic)
        self._ip = self._config_dic.pop("ip")

    def test(self):
        print("test in parent!")
        print(self._ip)