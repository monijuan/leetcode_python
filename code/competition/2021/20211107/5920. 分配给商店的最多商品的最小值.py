# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 11:20
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5920. 分配给商店的最多商品的最小值.py
# @Software: PyCharm 
# ===================================
"""给你一个整数 n ，表示有 n 间零售商店。总共有 m 种产品，每种产品的数目用一个下标从 0 开始的整数数组 quantities 表示，其中 quantities[i] 表示第 i 种商品的数目。

你需要将 所有商品 分配到零售商店，并遵守这些规则：

一间商店 至多 只能有 一种商品 ，但一间商店拥有的商品数目可以为 任意 件。
分配后，每间商店都会被分配一定数目的商品（可能为 0 件）。用 x 表示所有商店中分配商品数目的最大值，你希望 x 越小越好。也就是说，你想 最小化 分配给任意商店商品数目的 最大值 。
请你返回最小的可能的 x 。



示例 1：

输入：n = 6, quantities = [11,6]
输出：3
解释： 一种最优方案为：
- 11 件种类为 0 的商品被分配到前 4 间商店，分配数目分别为：2，3，3，3 。
- 6 件种类为 1 的商品被分配到另外 2 间商店，分配数目分别为：3，3 。
分配给所有商店的最大商品数目为 max(2, 3, 3, 3, 3, 3) = 3 。
示例 2：

输入：n = 7, quantities = [15,10,10]
输出：5
解释：一种最优方案为：
- 15 件种类为 0 的商品被分配到前 3 间商店，分配数目为：5，5，5 。
- 10 件种类为 1 的商品被分配到接下来 2 间商店，数目为：5，5 。
- 10 件种类为 2 的商品被分配到最后 2 间商店，数目为：5，5 。
分配给所有商店的最大商品数目为 max(5, 5, 5, 5, 5, 5, 5) = 5 。
示例 3：

输入：n = 1, quantities = [100000]
输出：100000
解释：唯一一种最优方案为：
- 所有 100000 件商品 0 都分配到唯一的商店中。
分配给所有商店的最大商品数目为 max(100000) = 100000 。


提示：

m == quantities.length
1 <= m <= n <= 105
1 <= quantities[i] <= 105
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def ceil(self,num):
        return int(num+1) if num>int(num) else int(num)

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        sum_all = sum(quantities)
        ave_min = self.ceil(sum_all/n)
        # 每个商品对应店铺数，按比例分
        num_box = [max(1,int(quant/ave_min)) for quant in quantities]
        remain_box = sum(num_box)-n

        # 剩余数量应该根据小数排序，从大到小分配

        print(num_box)
        res = [self.ceil(quant/box) for quant,box in zip(quantities,num_box)]
        return max(res)


def test(data_test):
    s = Solution()
    return s.minimizedMaximum(*data_test)


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
        [6,[11,6]],
        [7,[15,10,10]],
        [7,[13,11,11]],
        # [1,[100]],
        [3,[2,10,6]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')