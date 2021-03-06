# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 21:48
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day17_41. 数据流中的中位数.py
# @Software: PyCharm 
# ===================================
"""
"""
import time
from typing import List


class MedianFinder:
    def __init__(self):
        from sortedcontainers import SortedList
        self.length = 0
        self.datas = SortedList()
        self.mid = None

    def addNum(self, num: int) -> None:
        self.length+=1
        self.datas.add(num)
        self.mid = None

    def findMedian(self) -> float:
        if self.mid:
            return self.mid
        else:
            if self.length%2:
                self.mid = self.datas[(self.length-1)//2]
            else:
                right = self.length//2
                self.mid = sum(self.datas[right-1:right+1])/2
            return self.mid


def test(data_test):
    s = Solution()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = MedianFinder(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')