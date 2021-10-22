# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 13:42
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 229. 求众数 II.py
# @Software: PyCharm
# ===================================
"""给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

 

 

示例 1：

输入：[3,2,3]
输出：[3]
示例 2：

输入：nums = [1]
输出：[1]
示例 3：

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
 

提示：

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def majorityElement(self, nums: List[int]) -> List[int]:
        """摩尔投票法"""
        char_0,char_1,cnt_0,cnt_1 = None,None,0,0
        for num in nums:
            if cnt_0>0 and char_0==num:
                cnt_0+=1
            elif cnt_1>0 and char_1==num:
                cnt_1+=1
            elif cnt_0==0:
                char_0=num
                cnt_0=1
            elif cnt_1==0:
                char_1=num
                cnt_1=1
            else:
                cnt_0-=1
                cnt_1-=1

        cnt_res_0, cnt_res_1=0,0
        for num in nums:
            if cnt_0>0 and char_0==num:
                cnt_res_0+=1
            elif cnt_1>0 and char_1==num:
                cnt_res_1+=1
        res = []
        if cnt_0>0 and cnt_res_0>len(nums)/3:res.append(char_0)
        if cnt_1>0 and cnt_res_1>len(nums)/3:res.append(char_1)

        return res


def test(data_test):
    s = Solution()
    return s.majorityElement(*data_test)


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
        [[1,2]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
