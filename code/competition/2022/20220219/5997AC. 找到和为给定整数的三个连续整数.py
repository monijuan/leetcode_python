# -*- coding: utf-8 -*-
# @Time    : 2022/2/19 22:19
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5997AC. 找到和为给定整数的三个连续整数.py
# @Software: PyCharm 
# ===================================
"""给你一个整数 num ，请你返回三个连续的整数，它们的 和 为 num 。如果 num 无法被表示成三个连续整数的和，请你返回一个 空 数组。

 

示例 1：

输入：num = 33
输出：[10,11,12]
解释：33 可以表示为 10 + 11 + 12 = 33 。
10, 11, 12 是 3 个连续整数，所以返回 [10, 11, 12] 。
示例 2：

输入：num = 4
输出：[]
解释：没有办法将 4 表示成 3 个连续整数的和。
 

提示：

0 <= num <= 1015

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num//3 == num/3:
            return [num//3-1,num//3,num//3+1]
        else:
            return []


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.sumOfThree(*data)


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
        [4],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

