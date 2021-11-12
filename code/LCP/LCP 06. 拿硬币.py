# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 10:15
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 06. 拿硬币.py
# @Software: PyCharm
# ===================================
"""2020 春赛题集
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：

输入：[4,2,1]

输出：4

解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

示例 2：

输入：[2,3,10]

输出：8

限制：

1 <= n <= 4
1 <= coins[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/na-ying-bi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def ceil(self,num):
        return int(num+1) if num>int(num) else int(num)

    def minCount(self, coins: List[int]) -> int:
        return sum([int(self.ceil(x/2)) for x in coins])


def test(data_test):
    s = Solution()
    return s.minCount(*data_test)


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
        [[4,2,1]],
        [[2,3,10]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
