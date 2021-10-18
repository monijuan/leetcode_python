# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 10:47
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1009. 十进制整数的反码.py
# @Software: PyCharm
# ===================================
"""每个非负整数 N 都有其二进制表示。例如， 5 可以被表示为二进制 "101"，11 可以用二进制 "1011" 表示，依此类推。注意，除 N = 0 外，任何二进制表示中都不含前导零。

二进制的反码表示是将每个 1 改为 0 且每个 0 变为 1。例如，二进制数 "101" 的二进制反码为 "010"。

给你一个十进制数 N，请你返回其二进制表示的反码所对应的十进制整数。

 

示例 1：

输入：5
输出：2
解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。
示例 2：

输入：7
输出：0
解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。
示例 3：

输入：10
输出：5
解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"，也就是十进制中的 5 。
 

提示：

0 <= N < 10^9
本题与 476：https://leetcode-cn.com/problems/number-complement/ 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/complement-of-base-10-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
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


    def bitwiseComplement(self, n: int) -> int:
        if n==0:return 1
        str_b = self.二进制反码(n)
        while len(str_b) and str_b[0]=='0':str_b=str_b[1:]  # 去除前导零
        return self.二进制转十进制(str_b)

def test(data_test):
    s = Solution()
    return s.bitwiseComplement(*data_test)


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
        [0],
        [7],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
