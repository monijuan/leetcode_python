# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 15:03
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day24_57 - II. 和为s的连续正数序列.py
# @Software: PyCharm
# ===================================
"""输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def num_of_item(self,first,target):
        return (((2*first-1)**2+8*target)**0.5+1-2*first)/2

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        for first in range(1,target//2+1):
            length = self.num_of_item(first,target)
            if length%1==0:
                res.append([x for x in range(first,first+int(length))])
        return res


def test(data_test):
    s = Solution()
    return s.findContinuousSequence(*data_test)


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
        [9],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
