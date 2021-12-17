# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 14:05
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 040. 组合总和 II.py
# @Software: PyCharm
# ===================================
"""给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
 

提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def dfs(self,listnow,sumnow,idnow):
        if sumnow==self.target:
            self.res.append(listnow.copy())
        elif sumnow>self.target or idnow==self.length:
            return
        else:
            for next in range(idnow,self.length):
                if next>idnow and self.candidates[next]==self.candidates[next-1]:
                    continue
                next_num = self.candidates[next]
                listnow.append(next_num)
                self.dfs(listnow,sumnow+next_num,next+1)
                listnow.pop(-1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates,self.length,self.target = sorted(candidates),len(candidates),target
        self.res,self.vis = [],[False]*self.length
        self.dfs([],0,0)
        return self.res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.combinationSum2(*data)


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
        [[10,1,2,7,6,1,5],8],
        # [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],27],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
