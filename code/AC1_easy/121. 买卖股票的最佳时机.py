# -*- coding: utf-8 -*-
# @Time    : 2021/8/25 13:35
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 121. 买卖股票的最佳时机.py
# @Software: PyCharm
# ===================================
"""给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import sys
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_up = 0
        for price in prices:
            if price<min_price:
                min_price = min(min_price,price)
            else:
                max_up = max(max_up,price-min_price)
        return max_up


def test(data_test):
    s = Solution()
    return s.maxProfit(*data_test)


if __name__ == '__main__':
    datas = [
        [[7,1,5,3,6,4]],    # 5
        [[7,6,4,3,1]],  # 0
        [[59,13,1351,2133,5,35,3156,366,134,31,64,644,3313,16,4]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
