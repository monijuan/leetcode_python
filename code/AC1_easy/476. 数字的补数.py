# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 8:43
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 476. 数字的补数.py
# @Software: PyCharm
# ===================================
"""给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

 

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
 

提示：

给定的整数 num 保证在 32 位带符号整数的范围内。
num >= 1
你可以假定二进制数不包含前导零位。
本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-complement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def 二进制反码(self,num,s=''):
        if num==0:return s
        elif num%2:return self.二进制反码(num//2,'0'+s)
        else:return self.二进制反码(num//2,'1'+s)

    def 二进制转十进制(self,s):
        length = len(s)
        res = 0
        for i,num in enumerate(s):
            res += 0 if num=='0' else 2**(length-i-1)
        return res

    def findComplement(self, num: int) -> int:
        str_b = self.二进制反码(num)
        while len(str_b) and str_b[0]=='0':str_b=str_b[1:]  # 去除前导零
        return self.二进制转十进制(str_b)


def test(data_test):
    s = Solution()
    return s.findComplement(*data_test)


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
        [5],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
