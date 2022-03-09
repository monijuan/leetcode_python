# -*- coding: utf-8 -*-
# @Time    : 2022/3/9 8:48
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 798. 得分最高的最小轮调.py
# @Software: PyCharm
# ===================================
"""给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。

 

示例 1：

输入：nums = [2,3,1,4,0]
输出：3
解释：
下面列出了每个 k 的得分：
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
所以我们应当选择 k = 3，得分最高。
示例 2：

输入：nums = [1,3,0,2,4]
输出：0
解释：
nums 无论怎么变化总是有 3 分。
所以我们将选择最小的 k，即 0。
 

提示：

1 <= nums.length <= 105
0 <= nums[i] < nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class tree_树状数组:
    def __init__(self, n):
        self.n = n + 5
        self.sum = [0 for _ in range(n + 10)]
        self.ntimessum = [0 for _ in range(n + 10)]

    def _lowbit(self, x):
        return x & (-x)

    ### region 单点更新
    def add_pos(self, pos, k):
        """pos 单点更新 k"""
        x = pos
        while pos <= self.n:
            self.sum[pos] += k
            self.ntimessum[pos] += k * (x - 1)
            pos += self._lowbit(pos)

    def sum_pos_single(self, pos):
        """ 单点更新：1~pos 区间求和 """
        if not pos: return 0
        ret = 0
        while pos:
            ret += self.sum[pos]
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_single(self, l, r):
        """ 单点更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_single(r) - self.sum_pos_single(l - 1)

    def get_pos(self, pos):
        """ 单点更新：pos 单点查询 """
        return self.sum_pos_single(pos) - self.sum_pos_single(pos - 1)
    ####### endregion 单点更新

    ### region 区间更新
    def add_lr(self, l, r, k):
        """l~r 区间更新 k"""
        self.add_pos(l, k)
        self.add_pos(r + 1, -k)

    def sum_pos_internal(self, pos):
        """ 区间更新：1~pos 区间求和 """
        if not pos:
            return 0
        ret = 0
        x = pos
        while pos:
            ret += x * self.sum[pos] - self.ntimessum[pos]
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_internal(self, l, r):
        """ 区间更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_internal(r) - self.sum_pos_internal(l - 1)
    ####### endregion 区间更新

    def __str__(self):
        return f"sum:{self.sum}\n" \
               f"ntimessum:{self.ntimessum}"

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        """
        值<=新索引的  <=> x的新索引范围[x,l)
            x<=i: k的范围[i+1-l,i-x] <=> [0,i-x]+[i+1,l)
            i<x<l: k的范围(i-l,i-x] <=> [i+1,i-x+l]
            l<=x: 无解
        """
        l = len(nums)
        tree = tree_树状数组(l)
        for i,x in enumerate(nums):
            if x<=i:
                # print('x<=i',[i+1-l,i-x],i,x,0,i-x)
                tree.add_lr(0+1,i-x+1,1)
                if i+1<l:
                    # print('x<=i',[i+1-l,i-x],i,x,i+1,l-1)
                    tree.add_lr(i+1+1,l-1+1,1)
            elif i<x<l:
                # print('i<x<l',[i+1-l,i-x],i,x,i+1,i-x+l)
                tree.add_lr(i+1+1,i-x+l+1,1)
        sums = [tree.sum_pos_internal(i) for i in range(1,l+1)]
        scores = [s-sums[i-1] if i>0 else s for i,s in enumerate(sums) ]
        return scores.index(max(scores))



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.bestRotation(*data)


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
        [[2,3,1,4,0]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
