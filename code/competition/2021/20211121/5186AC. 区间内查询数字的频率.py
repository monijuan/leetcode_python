# -*- coding: utf-8 -*-
# @Time    : 2021/11/21 10:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5186AC. 区间内查询数字的频率.py
# @Software: PyCharm 
# ===================================
"""请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率 。

子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。

请你实现 RangeFreqQuery 类：

RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率 。
一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。



示例 1：

输入：
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
输出：
[null, 1, 2]

解释：
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。


提示：

1 <= arr.length <= 105
1 <= arr[i], value <= 104
0 <= left <= right < arr.length
调用 query 不超过 105 次。
"""
from leetcode_python.utils import *

class RangeFreqQuery:
    def __init__(self, arr: List[int]):
        self.dict = [[] for _ in range(10001)]
        for id,num in enumerate(arr):
            self.dict[num].append(id)


    def query(self, left: int, right: int, value: int) -> int:
        # print(f'query: {self.dict[value]} in range [{left},{right}]')
        nums = self.dict[value]
        length = len(nums)
        if length==0 or nums[-1]<left or nums[0]>right:return 0
        left_id,right_id = 0,length-1

        # 找>=left最小的数
        l,r=0,length-1
        while l<r:
            mid = (l + r) // 2
            if nums[mid] == left:
                left_id=mid
                break
            elif nums[mid] > left:
                r=mid
            else:
                l=mid+1
            if l==r:
                left_id = r
                break

        # 找<=right最大的数
        l,r=0,length-1
        while l<r:
            mid = (l + r+1) // 2
            if nums[mid] == right:
                right_id=mid
                break
            elif nums[mid] > right:
                r=mid-1
            else:
                l=mid
            if l==r:
                right_id = l
                break
        # print('left_id',left_id)
        # print('right_id',right_id)

        if right_id>left_id:
            return right_id-left_id+1
        elif left<=nums[left_id]<=right:
            return 1
        else:
            return 0


def test(data_test):
    s = RangeFreqQuery()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


def test_obj(data_test):
    result = [None]
    obj = RangeFreqQuery(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        # [["RangeFreqQuery","query","query"],[[[12,33,4,56,22,2,34,33,22,12,34,56]],[1,2,4],[0,11,33]]],
        # [["RangeFreqQuery","query","query"],[[[1,1,2,2,2,1,1,]],[1,5,2],[2,3,2]]],
        # [["RangeFreqQuery","query","query","query","query"],[[[1,1,1,2,2]],[0,1,2],[0,2,1],[3,3,2],[2,2,1]]],
        # [["RangeFreqQuery","query","query","query","query","query"],[[[3,4,5,3,3,2,2,2,5,4]],[2,6,3],[5,6,5],[1,6,2],[0,2,3],[5,6,4]]],
        [["RangeFreqQuery","query","query","query","query","query","query"],[[[8,4,2,5,4,5,8,6,2,3]],[0,3,5],[5,6,2],[6,8,4],[2,8,3],[4,5,1],[2,4,2]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')