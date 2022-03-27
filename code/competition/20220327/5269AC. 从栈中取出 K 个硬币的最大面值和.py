# -*- coding: utf-8 -*-
# @Time    : 2022/3/27 10:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5269AC. 从栈中取出 K 个硬币的最大面值和.py
# @Software: PyCharm 
# ===================================
"""一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币。

每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里。

给你一个列表 piles ，其中 piles[i] 是一个整数数组，分别表示第 i 个栈里 从顶到底 的硬币面值。同时给你一个正整数 k ，请你返回在 恰好 进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少 。



示例 1：



输入：piles = [[1,100,3],[7,8,9]], k = 2
输出：101
解释：
上图展示了几种选择 k 个硬币的不同方法。
我们可以得到的最大面值为 101 。
示例 2：

输入：piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
输出：706
解释：
如果我们所有硬币都从最后一个栈中取，可以得到最大面值和。


提示：

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 105
1 <= k <= sum(piles[i].length) <= 2000
"""
from leetcode_python.utils import *


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        last = [0] * (k + 1)
        for pile in piles:
            now = last[:]
            save = 0
            print(pile)
            for i, p in enumerate(pile):
                save += p
                print(f'i:{i},p:{p}')
                for j in range(i + 1, k + 1):
                    now[j] = max(now[j], last[j - (i + 1)] + save)
                    # print(f'j:{j},now:{now}')
                print(f'i:{i},p:{p},now:{now}')
            last = now
        return last[-1]

def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.maxValueOfCoins(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        [[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]],7],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
