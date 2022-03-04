# -*- coding: utf-8 -*-
# @Time    : 2022/3/2 8:55
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 564. 寻找最近的回文数.py
# @Software: PyCharm
# ===================================
"""给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

“最近的”定义为两个整数差的绝对值最小。

 

示例 1:

输入: n = "123"
输出: "121"
示例 2:

输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
 

提示:

1 <= n.length <= 18
n 只由数字组成
n 不含前导 0
n 代表在 [1, 1018 - 1] 范围内的整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-closest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length, int_n = len(n), int(n)
        if int_n < 10 or int_n == 10 ** (length-1): return str(int_n-1)
        if int_n - 1 == 10 ** (length-1): return str(int_n-2)
        if int_n + 1 == 10 ** length: return str(int_n + 2)

        pre = int(n[:(length+1)//2])
        tmp = [s[:length//2] + s[::-1] for s in [str(pre + dx) for dx in (-1, 0, 1)]]
        return min(tmp, key=lambda x: (x==n, abs(int(x)-int_n)))


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
