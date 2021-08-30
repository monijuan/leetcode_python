# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 21:57
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day08_63. 股票的最大利润.py
# @Software: PyCharm 
# ===================================
"""假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
import sys
from typing import List
# 本题与主站 121 题相同


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