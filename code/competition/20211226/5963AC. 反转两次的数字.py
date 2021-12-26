# -*- coding: utf-8 -*-
# @Time    : 2021/12/26 10:27
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5963AC. 反转两次的数字.py
# @Software: PyCharm 
# ===================================
"""反转 一个整数意味着倒置它的所有位。

例如，反转 2021 得到 1202 。反转 12300 得到 321 ，不保留前导零 。
给你一个整数 num ，反转 num 得到 reversed1 ，接着反转 reversed1 得到 reversed2 。如果 reversed2 等于 num ，返回 true ；否则，返回 false 。



示例 1：

输入：num = 526
输出：true
解释：反转 num 得到 625 ，接着反转 625 得到 526 ，等于 num 。
示例 2：

输入：num = 1800
输出：false
解释：反转 num 得到 81 ，接着反转 81 得到 18 ，不等于 num 。
示例 3：

输入：num = 0
输出：true
解释：反转 num 得到 0 ，接着反转 0 得到 0 ，等于 num 。


提示：

0 <= num <= 106
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def isSameAfterReversals(self, num: int) -> bool:
        if str(num)[-1]=='0' and num>0:return False
        else:return True


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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