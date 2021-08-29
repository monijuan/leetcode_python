# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 7:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1480. 一维数组的动态和.py
# @Software: PyCharm
# ===================================
"""
"""
import time
from typing import List

class Solution:
    def __init__(self):
        pass

    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if result:
                result.append(result[-1]+num)
            else:
                result.append(num)
        return result


def test(data_test):
    s = Solution()
    return s.runningSum(*data_test)

if __name__ == '__main__':
    datas = [
        [[1,2,3,4]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')