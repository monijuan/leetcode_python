# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 10:23
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 047. 全排列 II.py
# @Software: PyCharm
# ===================================
"""给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def dfs(self,now):
        if self.length>=len(now):
            if now not in self.res:
                self.res.append(now)
        else:
            for nextid in range(self.length):
                if not self.vis[nextid]:
                    self.vis[nextid]=True
                    self.dfs(now+[self.nums[nextid]])
                    self.vis[nextid]=False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.length = len(nums)
        self.vis = [False]*self.length
        self.res = []
        self.dfs([])
        return self.res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.permuteUnique(*data)


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
        # [[1,1,2]],
        [[1,1,0,0,1,-1,-1,1]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
