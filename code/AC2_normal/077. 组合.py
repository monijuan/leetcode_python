# -*- coding: utf-8 -*-
# @Time    : 2021/10/20 16:37
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 077. 组合.py
# @Software: PyCharm
# ===================================
"""给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]
 

提示：

1 <= n <= 20
1 <= k <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def dfs(self,numset,start):
        if len(numset)==self.k:
            if list(numset) not in self.res:
                self.res.append(list(numset))
        else:
            for num in range(start,self.n+1):
                if num not in numset:
                    numset.add(num)
                    self.dfs(numset,num+1)
                    numset.remove(num)

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.n = n
        self.k = k
        self.dfs(set(),1)
        return self.res


def test(data_test):
    s = Solution()
    return s.combine(*data_test)


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
        [4,2],
        [13,13],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
