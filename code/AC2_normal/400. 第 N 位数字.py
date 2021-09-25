# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 13:59
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 400. 第 N 位数字.py
# @Software: PyCharm 
# ===================================
"""在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。

 

注意：n 是正数且在 32 位整数范围内（n < 231）。

 

示例 1：

输入：3
输出：3
示例 2：

输入：11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nth-digit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def findNthDigit(self, n: int) -> int:
        save = [1, 10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8888888890, 98888888890]
        for length, ans in enumerate(save):
            if n+1 > ans: continue
            elif n + 1 == ans: return 9 if n else 0
            else: break
        remain = n - save[length - 1]
        res_num = 10 ** (length - 1) + remain // length
        return int(str(res_num)[remain % length])


def test(data_test):
    s = Solution()
    return s.findNthDigit(*data_test)


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