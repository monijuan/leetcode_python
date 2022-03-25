# -*- coding: utf-8 -*-
# @Time    : 2022/3/23 17:01
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 440. 字典序的第K小数字.py
# @Software: PyCharm 
# ===================================
"""给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

 

示例 1:

输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
示例 2:

输入: n = 1, k = 1
输出: 1
 

提示:

1 <= k <= n <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # 小于等于n的以1开头的数有多少个?
        # 1 10-19 100-199 1000-1999 = 1111
        def dfs(l, r):
            # 当前层有 r - l + 1 个节点可取，递归到下一层。
            # l * 10： 从10变成100， r * 10 + 9: 从19变成199
            return 0 if l > n else min(n, r) - l + 1 + dfs(l * 10, r * 10 + 9)

        cur = 1
        k -= 1
        while k:
            cnts = dfs(cur, cur)
            # 当前节点中总数都小于需要的数，可以全部取走，bfs到同层下一点 (比如 1 -> 2)
            if cnts <= k:
                k -= cnts
                cur += 1
            # 答案在当前节点的子节点中，取走当前根节点，dfs向下 (比如 1 -> 10)
            else:
                k -= 1
                cur *= 10
        return cur

def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
