# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 PM1:23
# @Author  : zhaohongjie@actionsky.com

def generate_large_mapfile(file):
    init = 10030000001
    with open(file, 'w') as f:
        for i in range(0,10500000):
            end=init + 9999
            line="{0}-{1}={2}\n".format(init, end, i%4)
            f.writelines(line)
            init = end+1


if __name__ == "__main__":
    generate_large_mapfile("output/myrule.txt")