# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 10:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6056AC. 字符串中最大的 3 位相同数字.py
# @Software: PyCharm 
# ===================================
"""给你一个字符串 num ，表示一个大整数。如果一个整数满足下述所有条件，则认为该整数是一个 优质整数 ：

该整数是 num 的一个长度为 3 的 子字符串 。
该整数由唯一一个数字重复 3 次组成。
以字符串形式返回 最大的优质整数 。如果不存在满足要求的整数，则返回一个空字符串 "" 。

注意：

子字符串 是字符串中的一个连续字符序列。
num 或优质整数中可能存在 前导零 。


示例 1：

输入：num = "6777133339"
输出："777"
解释：num 中存在两个优质整数："777" 和 "333" 。
"777" 是最大的那个，所以返回 "777" 。
示例 2：

输入：num = "2300019"
输出："000"
解释："000" 是唯一一个优质整数。
示例 3：

输入：num = "42352338"
输出：""
解释：不存在长度为 3 且仅由一个唯一数字组成的整数。因此，不存在优质整数。


提示：

3 <= num.length <= 1000
num 仅由数字（0 - 9）组成
"""
from leetcode_python.utils import *

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sss = ['999','888','777','666','555','444','333','222','111','000']
        for s in sss:
            if s in num:return s
        return ""


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
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
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
