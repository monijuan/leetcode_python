# -*- coding: utf-8 -*-
# @Time    : 2022/2/6 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6001AC. 重排数字的最小值.py
# @Software: PyCharm 
# ===================================
"""给你一个整数 num 。重排 num 中的各位数字，使其值 最小化 且不含 任何 前导零。

返回不含前导零且值最小的重排数字。

注意，重排各位数字后，num 的符号不会改变。



示例 1：

输入：num = 310
输出：103
解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。
不含任何前导零且值最小的重排数字是 103 。
示例 2：

输入：num = -7605
输出：-7650
解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。
不含任何前导零且值最小的重排数字是 -7650 。


提示：

-1015 <= num <= 1015
"""
from leetcode_python.utils import *


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        elif num<0:
            chars = list(str(-num))
            res = f'-{"".join(sorted(chars)[::-1])}'
            # res = f'-{"".join([str(x) for x in sorted(chars)][::-1])}'
        else:
            chars = sorted(list(str(num)))
            i = 0
            while i<len(chars) and chars[i]=='0':i+=1
            if i==len(chars)-1:
                res = chars[i] + '0' * i
            else:
                res = chars[i] + '0'*i + ''.join(chars[i+1:])
        return int(res)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.smallestNumber(*data)


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
        [7605],
        [1040010400],
        [0],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

