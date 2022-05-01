# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6048AC. 必须拿起的最小连续卡牌数.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 cards ，其中 cards[i] 表示第 i 张卡牌的 值 。如果两张卡牌的值相同，则认为这一对卡牌 匹配 。

返回你必须拿起的最小连续卡牌数，以使在拿起的卡牌中有一对匹配的卡牌。如果无法得到一对匹配的卡牌，返回 -1 。



示例 1：

输入：cards = [3,4,2,3,4,7]
输出：4
解释：拿起卡牌 [3,4,2,3] 将会包含一对值为 3 的匹配卡牌。注意，拿起 [4,2,3,4] 也是最优方案。
示例 2：

输入：cards = [1,0,5,3]
输出：-1
解释：无法找出含一对匹配卡牌的一组连续卡牌。


提示：

1 <= cards.length <= 105
0 <= cards[i] <= 106
"""
from leetcode_python.utils import *


def min_diss(nums):
    mindiss = float('inf')
    last = nums[0]
    for num in nums[1:]:
        mindiss = min(mindiss, num - last)
        last = num
    return mindiss+1


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        idx = defaultdict(list)
        for id, card in enumerate(cards):
            idx[card].append(id)
        res = float('inf')
        for card, ids in idx.items():
            if len(ids) > 1:
                res = min(res,min_diss(ids))
        return -1 if res == float('inf') else res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.minimumCardPickup(*data)


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
        [[3,4,2,3,4,7]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
