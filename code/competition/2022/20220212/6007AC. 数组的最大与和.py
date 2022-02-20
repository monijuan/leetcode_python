# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 21:01
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6007AC. 数组的最大与和.py
# @Software: PyCharm 
# ===================================
"""给你一个长度为 n 的整数数组 nums 和一个整数 numSlots ，满足2 * numSlots >= n 。总共有 numSlots 个篮子，编号为 1 到 numSlots 。

你需要把所有 n 个整数分到这些篮子中，且每个篮子 至多 有 2 个整数。一种分配方案的 与和 定义为每个数与它所在篮子编号的 按位与运算 结果之和。

比方说，将数字 [1, 3] 放入篮子 1 中，[4, 6] 放入篮子 2 中，这个方案的与和为 (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4 。
请你返回将 nums 中所有数放入 numSlots 个篮子中的最大与和。



示例 1：

输入：nums = [1,2,3,4,5,6], numSlots = 3
输出：9
解释：一个可行的方案是 [1, 4] 放入篮子 1 中，[2, 6] 放入篮子 2 中，[3, 5] 放入篮子 3 中。
最大与和为 (1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3) = 1 + 0 + 2 + 2 + 3 + 1 = 9 。
示例 2：

输入：nums = [1,3,10,4,7,1], numSlots = 9
输出：24
解释：一个可行的方案是 [1, 1] 放入篮子 1 中，[3] 放入篮子 3 中，[4] 放入篮子 4 中，[7] 放入篮子 7 中，[10] 放入篮子 9 中。
最大与和为 (1 AND 1) + (1 AND 1) + (3 AND 3) + (4 AND 4) + (7 AND 7) + (10 AND 9) = 1 + 1 + 3 + 4 + 7 + 8 = 24 。
注意，篮子 2 ，5 ，6 和 8 是空的，这是允许的。


提示：

n == nums.length
1 <= numSlots <= 9
1 <= n <= 2 * numSlots
1 <= nums[i] <= 15
"""
from leetcode_python.utils import *

def ppp(grid):
    print(np.array(grid))


class Solution_大佬:
    def maximumANDSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @lru_cache(None)
        def helper(i=0, s=tuple([0] * k)):
            if i == n: return 0
            t = list(s)
            ans = -float('inf')
            for j in range(k):
                if t[j] <= 1:
                    t[j] += 1
                    ans = max(ans, ((1 + j) & nums[i]) + helper(i + 1, tuple(t)))
                    t[j] -= 1
            return ans

        return helper()

### 赛后AC
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        res = 0
        @lru_cache(None)
        def dfs(s, i, cntj):
            nonlocal res
            if i == n:
                res = max(res,s)
                return 0
            cntj = list(cntj)
            for j in range(numSlots):
                if cntj[j] < 2:
                    cntj[j] += 1
                    dfs(s + (nums[i] & (j + 1)), i + 1, tuple(cntj))
                    cntj[j] -= 1
        dfs(0,0,tuple([0]*numSlots))
        return res

class Solution_wtl:
    @lru_cache(None)
    def dfs(self,s,i,cntj):
        if i==self.n:
            self.res = max(self.res,s)
            return
        cntj = list(cntj)
        for j in range(self.numSlots):
            if cntj[j]<2:
                # print(i,j,s,cntj)
                cntj[j]+=1
                self.dfs(s+self.grid[i][j],i+1,tuple(cntj))
                cntj[j]-=1

    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        self.numSlots = numSlots
        self.n = len(nums)
        self.res = 0
        self.grid = []
        for i in range(self.n):
            g = []
            for j in range(numSlots):
                g.append(nums[i]&(j+1))
            self.grid.append(g)
        # ppp(self.grid)
        cntj = [0]*numSlots
        for j in range(numSlots):
            cntj[j]+=1
            self.dfs(self.grid[0][j], 1, tuple(cntj))
            cntj[j]-=1
        return self.res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.maximumANDSum(*data)


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
        # [[14,7,9,8,2,4,11,1,9],8],
        [[11,9,3,10,2,5,11,8,12],7], # 23
        [[5,9,12,1,13,3,3,7,15,7,14,11,14],8], # 67
        # [[5,12,14,6,10,14,9,10,1,4,7],6], # 38
        [[1,2,3,4,5,6],3],
        # [[1,3,10,4,7,1],9],
        [[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9],9],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

