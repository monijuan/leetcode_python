# -*- coding: utf-8 -*-
# @Time    : 2021/12/19 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5958AC. 股票平滑下跌阶段的数目.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。

一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。

请你返回 平滑下降阶段 的数目。



示例 1：

输入：prices = [3,2,1,4]
输出：7
解释：总共有 7 个平滑下降阶段：
[3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1]
注意，仅一天按照定义也是平滑下降阶段。
示例 2：

输入：prices = [8,6,7,7]
输出：4
解释：总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7]
由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。
示例 3：

输入：prices = [1]
输出：1
解释：总共有 1 个平滑下降阶段：[1]


提示：

1 <= prices.length <= 105
1 <= prices[i] <= 105
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def getDescentPeriods(self, prices: List[int]) -> int:
        length = len(prices)
        res = [1]*length
        for id,price in enumerate(prices):
            if id>0 and price==prices[id-1]-1:
                res[id] = res[id-1]+1
        # print(res)
        return sum(res)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getDescentPeriods(*data)


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
        [[3,2,1,4]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')