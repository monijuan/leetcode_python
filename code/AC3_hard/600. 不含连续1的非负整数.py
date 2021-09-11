# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 6:39
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 600. 不含连续1的非负整数.py
# @Software: PyCharm 
# ===================================
"""给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例 1:

输入: 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
说明: 1 <= n <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findIntegers(self, n: int) -> int:
        """大佬"""
        res = 1
        num_b = bin(n)[2:]
        res_of_i = [1, 2]
        while len(res_of_i) <= len(num_b): res_of_i.append(res_of_i[-1] + res_of_i[-2])
        for i in range(len(num_b)):
            if i != len(num_b) - 1 and num_b[i] == num_b[i + 1] == '1':
                res += res_of_i[-i - 1] - 1
                break
            elif num_b[i] == '1':
                res += res_of_i[-i - 2]
        return res


    def findIntegers_暴力超时(self, n: int) -> int:
        res = 0
        for num in range(n+1):
            just_1 = False
            while num:
                if num&1:
                    if just_1: break
                    else: just_1=True
                else: just_1=False
                num=num//2
            else:
                res+=1
        return res


def test(data_test):
    s = Solution()
    return s.findIntegers(*data_test)


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
        # [5],
        # [10],
        # [100],
        # [1000],
        # [10000],
        [10000000],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')