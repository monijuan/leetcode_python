# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 14:35
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 295. 数据流的中位数.py
# @Software: PyCharm
# ===================================
"""中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例：

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
进阶:

如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-median-from-data-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List
from sortedcontainers import SortedList

class MedianFinder_超时:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.length = 0
        self.datas = []
        self.mid = None

    def addNum(self, num: int) -> None:
        self.length += 1
        self.datas.extend(num)
        self.mid = None

    def findMedian(self) -> float:
        if self.mid:
            return self.mid
        else:
            if self.length % 2:
                self.mid = sorted(self.datas)[(self.length + 1) // 2]
            else:
                left = self.length // 2
                self.mid = sum(sorted(self.datas)[left - 1:left + 1]) / 2
            return self.mid

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
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
    s = MedianFinder()
    return s.addNum(*data_test)


def test_obj(data_test):
    result = [None]
    obj = MedianFinder()
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        # print('command:',fun,data,res)
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"],
         [[],[1],[2],[],[3],[]]],
        # [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
