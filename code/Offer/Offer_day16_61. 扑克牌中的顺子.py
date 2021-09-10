# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 15:16
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day16_61. 扑克牌中的顺子.py
# @Software: PyCharm
# ===================================
"""从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def isStraight(self, nums: List[int]) -> bool:
        is_num = [0]*15
        cnt_0=0
        for x in nums:
            if is_num[x]:return False
            elif x: is_num[x]=1
            else: cnt_0+=1
        str_num=''.join([str(x) for x in is_num])
        num_of_need_0 = len(''.join(str_num.split('1')[1:-1]))
        return num_of_need_0<=cnt_0


def test(data_test):
    s = Solution()
    return s.isStraight(*data_test)


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
        [randListInt(0,13,5)],
        [randListInt(0,13,5)],
        [randListInt(0,13,5)],
        # [[0,0,2,2,5]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

    # for x in randListListInt(0,13,5,10):print(x)