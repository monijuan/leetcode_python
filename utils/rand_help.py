# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 21:28
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : rand_help.py
# @Software: PyCharm 
# ===================================
import random
from typing import List

def randListInt(smallest:int,biggest:int,length:int=10)->List[int]:
    """
    生成随机数列
    Args:
        smallest: 数列最小值
        biggest: 数列最大值
        length: 数列长度，默认20
    Returns:
        生成的随机数列
    """
    res = []
    while length:
        res.append(random.randint(smallest,biggest))
        length-=1
    return  res

def randListListInt(smallest:int,biggest:int,length:int=10,times:int=10)->List[List[int]]:
    return [randListInt(smallest,biggest,length) for _ in range(times)]

def randListListIntShow(*argvs):
    datas = randListListInt(*argvs)
    for x in datas:
        print(x)

if __name__ == '__main__':
    # datas = randListInt(1,30)
    # datas = randListListInt(0,10)
    # print(datas)
    # for x in datas:print(x)
    # randListListIntShow(1,30)
    data = randListListInt(smallest=-1000,biggest=1000,length=100)
    data = randListListInt(smallest=0,biggest=1000,length=100)
    print(data[0])