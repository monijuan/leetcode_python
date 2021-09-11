# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 15:10
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day30_51. 数组中的逆序对.py
# @Software: PyCharm 
# ===================================
"""在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)
        for i,num in enumerate(nums):
            res+=len([x for x in nums[i+1:length] if num>x])
        return res


def test(data_test):
    s = Solution()
    return s.reversePairs(data_test)


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
    # datas = [
    #     [[7,5,6,4]],
    # ]
    datas = [[814, 261, 334, 178, 574, 102, 285, 492, 272, 577, 526, 412, 273, 355, 125, 460, 414, 300, 619, 342], [403, 787, 65, 629, 603, 701, 831, 24, 516, 91, 137, 699, 24, 362, 222, 569, 317, 70, 887, 620], [720, 477, 421, 169, 787, 696, 413, 708, 556, 261, 170, 529, 179, 165, 558, 462, 494, 237, 860, 46], [489, 305, 689, 723, 284, 550, 112, 707, 645, 771, 427, 493, 301, 41, 554, 765, 700, 428, 666, 834], [186, 354, 419, 445, 161, 312, 192, 852, 546, 655, 888, 685, 714, 446, 44, 33, 762, 427, 34, 172], [665, 794, 562, 340, 708, 247, 251, 289, 232, 877, 371, 595, 360, 285, 669, 363, 562, 273, 730, 538], [362, 301, 441, 294, 478, 525, 523, 697, 515, 743, 564, 774, 170, 516, 510, 498, 349, 241, 93, 280], [564, 637, 777, 279, 709, 693, 311, 585, 127, 506, 662, 770, 422, 711, 412, 469, 172, 246, 316, 578], [57, 543, 798, 353, 687, 751, 494, 873, 830, 230, 58, 272, 838, 550, 802, 76, 332, 805, 797, 727], [728, 47, 456, 387, 227, 806, 232, 817, 827, 351, 346, 630, 52, 816, 706, 424, 462, 766, 781, 334]]

    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
    # print(randListListInt(1,888,20,10))
    # randListListIntShow(1,1888,49999,10)