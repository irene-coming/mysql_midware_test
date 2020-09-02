# -*- coding=utf-8 -*-
# Copyright (C) 2016-2020 ActionTech.
# License: https://www.mozilla.org/en-US/MPL/2.0 MPL version 2 or higher.
# @Time    : 2020/4/3 AM11:18
# @Author  : irene-coming
from Inherit.Parent import Parent


class Child(Parent):
    def __init__(self, config_dic):
        """
        test inherit of child
        """
        super(Child, self).__init__(config_dic)
        self._port = self._config_dic.pop("port")

    def test(self):
        print("test in child!")
        print(self._ip, self._port)