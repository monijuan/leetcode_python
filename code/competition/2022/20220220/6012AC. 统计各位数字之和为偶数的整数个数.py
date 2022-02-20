# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 10:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6012AC. 统计各位数字之和为偶数的整数个数.py
# @Software: PyCharm 
# ===================================
"""给你一个正整数 num ，请你统计并返回 小于或等于 num 且各位数字之和为 偶数 的正整数的数目。

正整数的 各位数字之和 是其所有位上的对应数字相加的结果。



示例 1：

输入：num = 4
输出：2
解释：
只有 2 和 4 满足小于等于 4 且各位数字之和为偶数。
示例 2：

输入：num = 30
输出：14
解释：
只有 14 个整数满足小于等于 4 且各位数字之和为偶数，分别是：
2、4、6、8、11、13、15、17、19、20、22、24、26 和 28 。


提示：

1 <= num <= 1000
"""
from leetcode_python.utils import *


class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1,num+1):
            if sum(int(c) for c in str(i))&1==0:
                res+=1
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.countEven(*data)


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
        [30],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

