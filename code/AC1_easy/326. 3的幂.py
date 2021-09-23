# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 20:52
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 326. 3的幂.py
# @Software: PyCharm 
# ===================================
"""给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

 

示例 1：

输入：n = 27
输出：true
示例 2：

输入：n = 0
输出：false
示例 3：

输入：n = 9
输出：true
示例 4：

输入：n = 45
输出：false
 

提示：

-231 <= n <= 231 - 1
 

进阶：

你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def isPowerOfThree(self, n: int) -> bool:
        if n==0:return False
        while n:
            if n==1:return True
            elif n%3!=0:return False
            temp=3
            while n%temp==0:
                n/=temp
                temp=temp**2


def test(data_test):
    s = Solution()
    return s.isPowerOfThree(*data_test)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')