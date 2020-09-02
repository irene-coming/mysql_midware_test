# -*- coding=utf-8 -*-
# Copyright (C) 2016-2020 ActionTech.
# License: https://www.mozilla.org/en-US/MPL/2.0 MPL version 2 or higher.
# @Time    : 2020/4/3 AM11:21
# @Author  : irene-coming
from Inherit.Child import Child
from Inherit.Parent import Parent

if __name__ == "__main__":
    param1 = {"ip":"127.0.0.1","port":"3306"}
    param2 = {"ip":"127.0.0.1"}
    param3 = "abc"

    parent = Parent(param1)
    parent.test()

    child = Child(param1)
    child.test()
