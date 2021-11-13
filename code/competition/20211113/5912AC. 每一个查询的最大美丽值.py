# -*- coding: utf-8 -*-
# @Time    : 2021/11/13 23:11
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5912AC. 每一个查询的最大美丽值.py
# @Software: PyCharm 
# ===================================
"""给你一个二维整数数组 items ，其中 items[i] = [pricei, beautyi] 分别表示每一个物品的 价格 和 美丽值 。

同时给你一个下标从 0 开始的整数数组 queries 。对于每个查询 queries[j] ，你想求出价格小于等于 queries[j] 的物品中，最大的美丽值 是多少。如果不存在符合条件的物品，那么查询的结果为 0 。

请你返回一个长度与 queries 相同的数组 answer，其中 answer[j]是第 j 个查询的答案。



示例 1：

输入：items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
输出：[2,4,5,5,6,6]
解释：
- queries[0]=1 ，[1,2] 是唯一价格 <= 1 的物品。所以这个查询的答案为 2 。
- queries[1]=2 ，符合条件的物品有 [1,2] 和 [2,4] 。
  它们中的最大美丽值为 4 。
- queries[2]=3 和 queries[3]=4 ，符合条件的物品都为 [1,2] ，[3,2] ，[2,4] 和 [3,5] 。
  它们中的最大美丽值为 5 。
- queries[4]=5 和 queries[5]=6 ，所有物品都符合条件。
  所以，答案为所有物品中的最大美丽值，为 6 。
示例 2：

输入：items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
输出：[4]
解释：
每个物品的价格均为 1 ，所以我们选择最大美丽值 4 。
注意，多个物品可能有相同的价格和美丽值。
示例 3：

输入：items = [[10,1000]], queries = [5]
输出：[0]
解释：
没有物品的价格小于等于 5 ，所以没有物品可以选择。
因此，查询的结果为 0 。


提示：

1 <= items.length, queries.length <= 105
items[i].length == 2
1 <= pricei, beautyi, queries[j] <= 109

"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def 找最大较小(self,q):
        if q<self.prices[0]:return 0
        elif q>self.prices[-1]:return self.prices[-1]
        left,right = 0,self.len_p-1
        while left<right:
            mid = left + (right-left)//2
            mid_p = self.prices[mid]
            if mid_p==q:return mid_p
            elif mid_p<=q and self.prices[mid+1]>q:return mid_p
            elif mid_p>q and self.prices[mid-1]<=q:return self.prices[mid-1]
            elif mid_p>q:right=mid-1
            else:left=mid+1
        if self.prices[right]<=q:return self.prices[right]
        elif self.prices[right]>q and self.prices[left]<=q:return self.prices[left]
        else:return 0

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        beauty = {}
        for p,b in items:
            beauty[p] = max(b,beauty.get(p,0))

        self.prices = sorted(beauty.keys())
        self.len_p = len(self.prices)
        # print(queries)
        last_max = 0
        for p in self.prices:
            last_max = max(last_max,beauty[p])
            beauty[p]= last_max
            # print(p,beauty[p])
        # print([self.找最大较小(q) for q in queries])
        res = [beauty.get(self.找最大较小(q),0) for q in queries]
        # print(res)
        return res


def test(data_test):
    s = Solution()
    return s.maximumBeauty(*data_test)


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
        # [[[1,2],[3,2],[2,4],[5,6],[3,5]],[1,2,3,4,5,6]],
        [[[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]],[885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')