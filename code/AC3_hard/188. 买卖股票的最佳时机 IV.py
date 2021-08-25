# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 14:49
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 188. 买卖股票的最佳时机 IV.py
# @Software: PyCharm
# ===================================
"""给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
 

提示：

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        if length < 2 or k < 1: return 0
        times = k if 2*k<=length else length//2   # 卖出次数不会超过一半天数
        buy = [-prices[0]] * times      # buy[i] 表示第i次买入后的最大 Profit
        sell = [0] * times              # sell[i]表示第i次卖出后的最大 Profit
        for price in prices:
            for time in range(times):
                if time == 0:
                    buy[time] = max(buy[time], -price)  # 初始状态
                else:
                    buy[time] = max(buy[time], sell[time - 1] - price)  # 买入操作
                sell[time] = max(sell[time], buy[time] + price)  # 卖出操作
        return sell[-1]

def test(data_test):
    s = Solution()
    return s.maxProfit(*data_test)


if __name__ == '__main__':
    datas = [
        [2,[2,4,1]],# 2
        [2,[3,2,6,5,0,3]],# 7
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
