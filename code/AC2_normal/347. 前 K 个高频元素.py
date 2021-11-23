# -*- coding: utf-8 -*-
# @Time    : 2021/11/23 9:13
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 347. 前 K 个高频元素.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import collections

from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = sorted(list(collections.Counter(nums).items()),key=lambda x:-x[1])
        print(cnt)
        return [x[0] for x in cnt[:k]]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.topKFrequent(*data)


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
        [[1,1,1,2,2,3],2],
        [[12, 47, 43, 1, 45, 50, 20, 48, 17, 44, 25, 21, 41, 38, 15, 9, 40, 43, 20, 13, 1, 13, 44, 40, 48, 33, 41, 17, 33, 31, 39, 45, 7, 5, 50, 4, 36, 36, 30, 11, 31, 10, 46, 18, 47, 0, 26, 44, 26, 6, 45, 15, 10, 24, 44, 5, 8, 4, 25, 2, 11, 29, 24, 25, 28, 45, 43, 20, 21, 11, 19, 44, 23, 32, 33, 45, 35, 48, 44, 36, 25, 48, 18, 1, 18, 28, 37, 10, 25, 39, 29, 27, 41, 17, 12, 16, 3, 6, 44, 8],5],
        [[334, 146, 717, 401, 410, 622, 555, 588, 564, 711, 403, 177, 504, 223, 155, 881, 302, 196, 764, 829, 873, 326, 397, 564, 231, 205, 271, 564, 43, 954, 66, 534, 62, 474, 860, 636, 269, 808, 803, 433, 457, 57, 670, 968, 184, 890, 687, 556, 749, 423, 505, 189, 756, 198, 995, 91, 921, 55, 171, 240, 895, 343, 887, 20, 176, 95, 114, 715, 502, 660, 396, 907, 585, 886, 962, 317, 352, 591, 488, 69, 572, 108, 915, 837, 250, 135, 31, 389, 676, 208, 41, 859, 114, 140, 191, 503, 670, 266, 59, 548],5],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
