# -*- coding: utf-8 -*-
# @Time    : 2022/1/22 21:34
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5971AC. 打折购买糖果的最小开销.py
# @Software: PyCharm 
# ===================================
"""一家商店正在打折销售糖果。每购买 两个 糖果，商店会 免费 送一个糖果。

免费送的糖果唯一的限制是：它的价格需要小于等于购买的两个糖果价格的 较小值 。

比方说，总共有 4 个糖果，价格分别为 1 ，2 ，3 和 4 ，一位顾客买了价格为 2 和 3 的糖果，那么他可以免费获得价格为 1 的糖果，但不能获得价格为 4 的糖果。
给你一个下标从 0 开始的整数数组 cost ，其中 cost[i] 表示第 i 个糖果的价格，请你返回获得 所有 糖果的 最小 总开销。



示例 1：

输入：cost = [1,2,3]
输出：5
解释：我们购买价格为 2 和 3 的糖果，然后免费获得价格为 1 的糖果。
总开销为 2 + 3 = 5 。这是开销最小的 唯一 方案。
注意，我们不能购买价格为 1 和 3 的糖果，并免费获得价格为 2 的糖果。
这是因为免费糖果的价格必须小于等于购买的 2 个糖果价格的较小值。
示例 2：

输入：cost = [6,5,7,9,2,2]
输出：23
解释：最小总开销购买糖果方案为：
- 购买价格为 9 和 7 的糖果
- 免费获得价格为 6 的糖果
- 购买价格为 5 和 2 的糖果
- 免费获得价格为 2 的最后一个糖果
因此，最小总开销为 9 + 7 + 5 + 2 = 23 。
示例 3：

输入：cost = [5,5]
输出：10
解释：由于只有 2 个糖果，我们需要将它们都购买，而且没有免费糖果。
所以总最小开销为 5 + 5 = 10 。
"""
from leetcode_python.utils import *


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        while len(cost)%3:cost.append(0)
        res = 0
        for i in range(0,len(cost),3):
            res +=(cost[i]+cost[i+1])
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.minimumCost(*data)


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
        [[6,5,7,9,2,2]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')