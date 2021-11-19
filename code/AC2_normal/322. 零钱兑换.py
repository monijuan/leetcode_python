# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 15:52
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 322. 零钱兑换.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        超时case：[411,412,413,414,415,416,417,418,419,420,421,422],9864
        超时case：[3,7,405,436],8839
        超时case：[2,4,6,8,10,12,14,16,18,20,22,24],9999
        """
        self.remain_count_dict = {}
        pass

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

        ######## 也超时
    @lru_cache(None)
    def dfs_check_超时2(self, remain, count, index):
        if remain==0:
            self.res = min(self.res,count)
            return
        elif index == self.length or self.vi[remain][index]<=count:
            return
        else:
            coin_now = self.coins[index]
            for cnt_now in range(remain//coin_now,-1,-1):   # 注意range左闭右开
                if cnt_now+count>=self.res:break
                self.dfs_check_超时2(remain-cnt_now*self.coins[index],count+cnt_now,index+1)
            self.vi[remain][index] = min(self.vi[remain][index],count)

    def coinChange_超时2(self, coins: List[int], amount: int) -> int:
        self.res = float('inf')
        self.length = len(coins)
        self.coins = sorted(coins,reverse=True)
        self.vi = [[float('inf')]*self.length for _ in range(amount+1)]
        self.dfs_check_超时2(amount,0,0)
        return -1 if self.res==float('inf') else self.res

    ######## 超时
    @lru_cache(None)
    def dfs_check_超时(self,remain,count,index):
        # print(f'remain:{remain}, count:{count}, index:{index}, nowres:{self.res}')
        if remain==0:
            self.res = min(self.res,count)
            return
        elif index == self.length or self.remain_count_dict.get(remain,float('inf'))<count:
            # print('return')
            return
        else:
            self.remain_count_dict[remain]=count
            coin_now = self.coins[index]
            for cnt_now in range(remain//coin_now,-1,-1):   # 注意range左闭右开
                if cnt_now+count>=self.res:break
            # for cnt_now in range(remain//coin_now+1):
            #     if cnt_now+count>=self.res:continue # 从小到大会超时
                self.dfs_check_超时(remain-cnt_now*self.coins[index],count+cnt_now,index+1)

    def coinChange_超时(self, coins: List[int], amount: int) -> int:
        self.res = float('inf')
        self.length = len(coins)
        self.coins = sorted(coins,reverse=True)
        self.dfs_check_超时(amount,0,0)
        return -1 if self.res==float('inf') else self.res


def test(data_test):
    s = Solution()
    # return s.coinChange_超时(*data_test)
    return s.coinChange(*data_test)


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
        # [[1,2,5],11],
        # [[411,412,413,414,415,416,417,418,419,420,421,422],3000],
        # [[411,412,413,414,415,416,417,418,419,420,421,422],9864],
        # [[3,7,405,436],8839],
        # [[484,395,346,103,329],4259],
        [[2,4,6,8,10,12,14,16,18,20,22,24],3333],
        # [[2,4,6,8,10,12,14,16,18,20,22,24],9999],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
