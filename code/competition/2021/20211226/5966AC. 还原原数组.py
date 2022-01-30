# -*- coding: utf-8 -*-
# @Time    : 2021/12/26 10:27
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5966AC. 还原原数组.py
# @Software: PyCharm 
# ===================================
"""Alice 有一个下标从 0 开始的数组 arr ，由 n 个正整数组成。她会选择一个任意的 正整数 k 并按下述方式创建两个下标从 0 开始的新整数数组 lower 和 higher ：

对每个满足 0 <= i < n 的下标 i ，lower[i] = arr[i] - k
对每个满足 0 <= i < n 的下标 i ，higher[i] = arr[i] + k
不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 lower 和 higher 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。

给你一个由 2n 个整数组成的整数数组 nums ，其中 恰好 n 个整数出现在 lower ，剩下的出现在 higher ，还原并返回 原数组 arr 。如果出现答案不唯一的情况，返回 任一 有效数组。

注意：生成的测试用例保证存在 至少一个 有效数组 arr 。



示例 1：

输入：nums = [2,10,6,4,8,12]
输出：[3,7,11]
解释：
如果 arr = [3,7,11] 且 k = 1 ，那么 lower = [2,6,10] 且 higher = [4,8,12] 。
组合 lower 和 higher 得到 [2,6,10,4,8,12] ，这是 nums 的一个排列。
另一个有效的数组是 arr = [5,7,9] 且 k = 3 。在这种情况下，lower = [2,4,6] 且 higher = [8,10,12] 。
示例 2：

输入：nums = [1,1,3,3]
输出：[2,2]
解释：
如果 arr = [2,2] 且 k = 1 ，那么 lower = [1,1] 且 higher = [3,3] 。
组合 lower 和 higher 得到 [1,1,3,3] ，这是 nums 的一个排列。
注意，数组不能是 [1,3] ，因为在这种情况下，获得 [1,1,3,3] 唯一可行的方案是 k = 0 。
这种方案是无效的，k 必须是一个正整数。
示例 3：

输入：nums = [5,435]
输出：[220]
解释：
唯一可行的组合是 arr = [220] 且 k = 215 。在这种情况下，lower = [5] 且 higher = [435] 。


提示：

2 * n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 109
生成的测试用例保证存在 至少一个 有效数组 arr
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def tryd(self,d,nums):
        print('try d',d)
        res = []
        vis = [False]*self.length
        for i,n in enumerate(nums):
            # print(vis,res)
            if vis[i]:continue
            vis[i]=True
            p = n+d
            idp = bisect.bisect_left(nums,p)
            if idp<len(nums)and nums[idp]==p :
                while idp<self.length and vis[idp]:
                    idp+=1
                if idp>=self.length or nums[idp]!=p:
                    return False
                else:
                    res.append((n+p)//2)
                    vis[idp]=True
            else:
                return False
        return res


    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        self.length =  len(nums)
        cnt_dis_d = defaultdict(int)
        for i in range(self.length):
            for j in range(i+1,self.length):
                cnt_dis_d[nums[j]-nums[i]]+=1
        # for n,c in cnt_dis_d.items():
        #     print(n,c)
        d_may = [d for d,c in cnt_dis_d.items() if c>=self.length//2 and d&1==0 and d>0]
        print('d_may',d_may)
        for d in d_may:
            res = self.tryd(d,nums)
            if res:return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.recoverArray(*data)


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
        # [[2,10,6,4,8,12]],
        # [[1,1,3,3]],
        # [[11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]], # [2,3,7,8,8,9,9,10]
        [[3,7,7,1,5,3]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')