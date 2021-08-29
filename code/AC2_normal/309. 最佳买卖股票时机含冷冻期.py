# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 15:34
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 309. 最佳买卖股票时机含冷冻期.py
# @Software: PyCharm
# ===================================
"""给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        """
        三种历史状态：
        last_buy ： 上次买了（包括之前就买了的情况）的最大收益；
        last_sell ： 上次刚卖，现在是冷冻期；
        last_frozen ： 上上次卖了（包括再之前就卖了的情况），意味着现在可以买；
        三种当前状态：

        hold_on：比较【last_buy（继续持有）】【last_frozen（如果没有卖）】；
        sell：不用比较，就是之前持有的状态+现在的价格；
        can_buy：比较【last_sell（上次之前已经卖了的）】【last_frozen（刚过冷冻期的）】；
        三种变化：

        已经买入 ：比较之前已经卖了收益大，还是 上上次卖出（上次刚解冻）-当前价格 收益
        冷冻期中 = 如果上次是买入状态 + 当前价格
        可以买入(过了冷冻期) ：比较之前已经卖了收益大，还是才刚刚卖了的收益大

        作者：1019646292
        链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/python3309-zui-jia-mai-mai-gu-piao-shi-j-bfx5/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        """
        pass

    def maxProfit(self, prices: List[int]) -> int:
        last_buy = -prices[0]
        last_sell = 0
        last_frozen = 0
        for price in prices[1::]:
            hold_on = max(last_buy,last_frozen-price)   # 已经买入 ：比较之前已经卖了收益大，还是 上上次卖出（上次刚解冻）-当前价格 收益大
            sell = last_buy + price                  # 冷冻期中 = 如果上次是买入状态 + 当前价格
            can_buy = max(last_sell,last_frozen)     # 可以买入(过了冷冻期) ：比较之前已经卖了收益大，还是才刚刚卖了的收益大
            last_buy, last_sell, last_frozen = hold_on, sell, can_buy

        return max(last_sell,last_frozen)


def test(data_test):
    s = Solution()
    return s.maxProfit(*data_test)


if __name__ == '__main__':
    datas = [
        [[1,2,3,0,2]],# 3
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
