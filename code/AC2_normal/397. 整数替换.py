# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 8:50
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 397. 整数替换.py
# @Software: PyCharm
# ===================================
"""给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
n 变为 1 所需的最小替换次数是多少？

 

示例 1：

输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1
示例 2：

输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1
示例 3：

输入：n = 4
输出：2
 

提示：

1 <= n <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-replacement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
            if n==3:
                res+=2
                break
            elif n%4==3:
                res += 2
                n = n // 2 + 1
            else:
                res += (1+int(n%2))
                n //= 2
        return res

    def integerReplacement2(self, n: int) -> int:
        res = 0
        while n != 1:
            if n % 2 == 0:
                res += 1
                n //= 2
            elif n % 4 == 1:
                res += 2
                n //= 2
            else:
                if n == 3:
                    res += 2
                    n = 1
                else:
                    res += 2
                    n = n // 2 + 1
        return res



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.integerReplacement(*data)


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
        [4],
        [5],
        [6],
        [7],
        [10],
        [99],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
