# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 22:24
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6024AC. 数组中紧跟 key 之后出现最频繁的数字.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的整数数组 nums ，同时给你一个整数 key ，它在 nums 出现过。

统计 在 nums 数组中紧跟着 key 后面出现的不同整数 target 的出现次数。换言之，target 的出现次数为满足以下条件的 i 的数目：

0 <= i <= n - 2
nums[i] == key 且
nums[i + 1] == target 。
请你返回出现 最多 次数的 target 。测试数据保证出现次数最多的 target 是唯一的。



示例 1：

输入：nums = [1,100,200,1,100], key = 1
输出：100
解释：对于 target = 100 ，在下标 1 和 4 处出现过 2 次，且都紧跟着 key 。
没有其他整数在 key 后面紧跟着出现，所以我们返回 100 。
示例 2：

输入：nums = [2,2,2,2,3], key = 2
输出：2
解释：对于 target = 2 ，在下标 1 ，2 和 3 处出现过 3 次，且都紧跟着 key 。
对于 target = 3 ，在下标 4 出出现过 1 次，且紧跟着 key 。
target = 2 是紧跟着 key 之后出现次数最多的数字，所以我们返回 2 。


提示：

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
测试数据保证答案是唯一的。
"""
from leetcode_python.utils import *


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnts = defaultdict(int)
        for i,n in enumerate(nums):
            if n==key and i<len(nums)-1:
                cnts[nums[i+1]]+=1
        res = sorted(cnts.items(),key=lambda x:-x[1])
        return res[0][0]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.mostFrequent(*data)


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
        [[1,100,200,1,100],1],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

