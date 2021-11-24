# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 11:31
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 483. 最小好进制.py
# @Software: PyCharm
# ===================================
"""对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

 

示例 1：

输入："13"
输出："3"
解释：13 的 3 进制是 111。
示例 2：

输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
示例 3：

输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
 

提示：

n的取值范围是 [3, 10^18]。
输入总是有效且没有前导 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-good-base
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *
import math

class Solution:
    def __init__(self):
        pass

    def smallestGoodBase(self, n: str) -> str:
        SUM = int(n)
        for 位数 in range(int(math.log2(SUM))+1,1,-1):  # 2进制时有 int(math.log2(SUM+1) 个1
            进制 = max(2,int(SUM ** (1 / 位数)))
            求和 = (进制 ** (位数+1) - 1) // (进制 - 1)
            # print(位数,进制,求和)
            if 求和==SUM: return str(进制)
        return str(SUM-1)

    def smallestGoodBase_超时(self, n: str) -> str:
        SUM = int(n)
        for 位数 in range(int(math.log2(SUM)),1,-1):  # 2进制时有 int(math.log2(SUM+1) 个1
            for 进制 in range(2,SUM):
                求和 = int((进制**位数-1)/(进制-1))
                if 求和==SUM:return str(进制)
                elif 求和>SUM:break
        return str(SUM-1)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.smallestGoodBase(*data)


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
        # ["127"],  # 1111111   64+32+16+8+4+2+1
        # ["156"],    # 1111  125+25+5+1
        # ["781"],
        # ["3541"],
        # ["4681"],
        # ["4681"],
        ["14919921443713777"],
        # ["35184372088832"],
        # ["35184372088831"],
        # ["1000000000000000000"],
        # ["315468716547000000"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
