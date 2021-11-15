# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 18:37
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 377. 组合总和 Ⅳ.py
# @Software: PyCharm 
# ===================================
"""给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

 

示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000
 

进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count_for_target = [1] + [0]*target
        for target_temp in range(1,target+1):
            for num in nums:
                if num<= target_temp:
                    count_for_target[target_temp] += count_for_target[target_temp-num]
        return count_for_target[-1]

    def dfs_超时(self, now):
        for num in self.nums:
            next = now + num
            if next == self.target:
                self.res += 1
            elif next < self.target:
                self.dfs(next)
            else:
                break

    def combinationSum4_超时(self, nums: List[int], target: int) -> int:
        """
        输入：[[4, 2, 1], 32]
        结果：39882198
        会超时
        """
        self.nums = sorted(nums)
        self.target = target
        self.res = 0
        self.dfs_超时(0)
        return self.res


def test(data_test):
    s = Solution()
    return s.combinationSum4(*data_test)


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
        [[4,2,1],32],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')