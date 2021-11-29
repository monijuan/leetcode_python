# -*- coding: utf-8 -*-
# @Time    : 2021/11/27 22:24
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5923. 从房屋收集雨水需要的最少水桶数.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的字符串 street 。street 中每个字符要么是表示房屋的 'H' ，要么是表示空位的 '.' 。

你可以在 空位 放置水桶，从相邻的房屋收集雨水。位置在 i - 1 或者 i + 1 的水桶可以收集位置为 i 处房屋的雨水。一个水桶如果相邻两个位置都有房屋，那么它可以收集 两个 房屋的雨水。

在确保 每个 房屋旁边都 至少 有一个水桶的前提下，请你返回需要的 最少 水桶数。如果无解请返回 -1 。



示例 1：

输入：street = "H..H"
输出：2
解释：
我们可以在下标为 1 和 2 处放水桶。
"H..H" -> "HBBH"（'B' 表示放置水桶）。
下标为 0 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。
示例 2：

输入：street = ".H.H."
输出：1
解释：
我们可以在下标为 2 处放置一个水桶。
".H.H." -> ".HBH."（'B' 表示放置水桶）。
下标为 1 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。
示例 3：

输入：street = ".HHH."
输出：-1
解释：
没有空位可以放置水桶收集下标为 2 处的雨水。
所以没有办法收集所有房屋的雨水。
示例 4：

输入：street = "H"
输出：-1
解释：
没有空位放置水桶。
所以没有办法收集所有房屋的雨水。
示例 5：

输入：street = "."
输出：0
解释：
没有房屋需要收集雨水。
所以需要 0 个水桶。


提示：

1 <= street.length <= 105
street[i] 要么是 'H' ，要么是 '.' 。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def minimumBuckets(self, street: str) -> int:
        if len(street)==1:
            return 0 if street=="." else -1
        elif street[:2]=="HH":
            return -1
        res = 0
        left = street[0]
        for i in range(1,len(street)-1):
            now = street[i-1:i+1]
            if now=='HHH':return -1
            elif now=='HH.':res+=1
            elif now=='H.H':res+=1
            elif now=='.HH':pass


        return


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
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