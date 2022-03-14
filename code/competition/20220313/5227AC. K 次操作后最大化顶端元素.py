# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 21:56
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5227AC. K 次操作后最大化顶端元素.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的整数数组 nums ，它表示一个 栈 ，其中 nums[0] 是栈顶的元素。

每一次操作中，你可以执行以下操作 之一 ：

如果栈非空，那么 删除 栈顶端的元素。
如果有超过 1 个或者多个被删除且不在栈中的元素，你可以从它们中选择任何一个，添加 回栈顶，这个元素成为新的栈顶元素。
同时给你一个整数 k ，它表示你总共需要执行操作的次数。

请你返回 恰好 执行 k 次操作以后，栈顶元素的 最大值 。如果执行完 k 次操作以后，栈一定为空，请你返回 -1 。



示例 1：

输入：nums = [5,2,2,4,0,6], k = 4
输出：5
解释：
4 次操作后，栈顶元素为 5 的方法之一为：
- 第 1 次操作：删除栈顶元素 5 ，栈变为 [2,2,4,0,6] 。
- 第 2 次操作：删除栈顶元素 2 ，栈变为 [2,4,0,6] 。
- 第 3 次操作：删除栈顶元素 2 ，栈变为 [4,0,6] 。
- 第 4 次操作：将 5 添加回栈顶，栈变为 [5,4,0,6] 。
注意，这不是最后栈顶元素为 5 的唯一方式。但可以证明，4 次操作以后 5 是能得到的最大栈顶元素。
示例 2：

输入：nums = [2], k = 1
输出：-1
解释：
第 1 次操作中，我们唯一的选择是将栈顶元素弹出栈。
由于 1 次操作后无法得到一个非空的栈，所以我们返回 -1 。


提示：

1 <= nums.length <= 105
0 <= nums[i], k <= 109
"""
from leetcode_python.utils import *


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k==0:return nums[0]
        elif len(nums)==1 and k&1:return -1
        elif k==1:return nums[1]
        elif k>len(nums):return max(nums)
        else:
            nums.pop(k-1)
            return max(nums[:k])

        l1,l2 = [],[]
        for i in range(0,min(k,len(nums)),2):
            l1.append(nums[i])
            if i+1<len(nums):
                l2.append(nums[i+1])
        if k<len(nums):
            if k&1: l2.append(nums[k])
            else: l1.append(nums[k])
        print(l1)
        print(l2)
        if k&1:
            if l2:return max(l2)
        else:
            if l1:return max(l1)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.maximumTop(*data)


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
        [[5,2,2,4,0,6],4],
        [[2],1],
        [[99,95,68,24,18],69],
        [[35,43,23,86,23,45,84,2,18,83,79,28,54,81,12,94,14,0,0,29,94,12,13,1,48,85,22,95,24,5,73,10,96,97,72,41,52,1,91,3,20,22,41,98,70,20,52,48,91,84,16,30,27,35,69,33,67,18,4,53,86,78,26,83,13,96,29,15,34,80,16,49],15],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

