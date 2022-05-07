# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 9:05
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1201. 丑数 III.py
# @Software: PyCharm 
# ===================================
"""给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的 正整数 。

 

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
 

提示：

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
本题结果在 [1, 2 * 10^9] 的范围内

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm3(x, y, z):
            a = (x * y) // math.gcd(x, y)
            return (a * z) // math.gcd(a, z)

        def uglynum(x):
            return x // a + x // b + x // c - x // (a * b // math.gcd(a, b)) - x // (a * c // math.gcd(a, c)) - x // (
                    b * c // math.gcd(b, c)) + x // lcm3(a, b, c)

        left, right = 1, n * min(a, b, c)

        while left < right:
            mid = (left + right) >> 1
            if uglynum(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
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
