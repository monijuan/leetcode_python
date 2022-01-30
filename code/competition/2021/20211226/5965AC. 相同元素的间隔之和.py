# -*- coding: utf-8 -*-
# @Time    : 2021/12/26 10:27
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5965AC. 相同元素的间隔之和.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始、由 n 个整数组成的数组 arr 。

arr 中两个元素的 间隔 定义为它们下标之间的 绝对差 。更正式地，arr[i] 和 arr[j] 之间的间隔是 |i - j| 。

返回一个长度为 n 的数组 intervals ，其中 intervals[i] 是 arr[i] 和 arr 中每个相同元素（与 arr[i] 的值相同）的 间隔之和 。

注意：|x| 是 x 的绝对值。



示例 1：

输入：arr = [2,1,3,1,2,3,3]
输出：[4,2,7,2,4,4,5]
解释：
- 下标 0 ：另一个 2 在下标 4 ，|0 - 4| = 4
- 下标 1 ：另一个 1 在下标 3 ，|1 - 3| = 2
- 下标 2 ：另两个 3 在下标 5 和 6 ，|2 - 5| + |2 - 6| = 7
- 下标 3 ：另一个 1 在下标 1 ，|3 - 1| = 2
- 下标 4 ：另一个 2 在下标 0 ，|4 - 0| = 4
- 下标 5 ：另两个 3 在下标 2 和 6 ，|5 - 2| + |5 - 6| = 4
- 下标 6 ：另两个 3 在下标 2 和 5 ，|6 - 2| + |6 - 5| = 5
示例 2：

输入：arr = [10,5,10,10]
输出：[5,0,3,4]
解释：
- 下标 0 ：另两个 10 在下标 2 和 3 ，|0 - 2| + |0 - 3| = 5
- 下标 1 ：只有这一个 5 在数组中，所以到相同元素的间隔之和是 0
- 下标 2 ：另两个 10 在下标 0 和 3 ，|2 - 0| + |2 - 3| = 3
- 下标 3 ：另两个 10 在下标 0 和 2 ，|3 - 0| + |3 - 2| = 4


提示：

n == arr.length
1 <= n <= 105
1 <= arr[i] <= 105
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def getDistances(self, arr: List[int]) -> List[int]:
        num_idli = defaultdict(list)
        for id,num in enumerate(arr):
            num_idli[num].append(id)
        res = [0]*len(arr)
        for li in num_idli.values():
            s,sumli = 0,[]
            for x in li:
                s+=x
                sumli.append(s)
            l = len(li)
            for i,(s,n) in enumerate(zip(sumli,li)):
                # rl =  (n+i*n-s) if i>0 else 0
                rl =  n+i*n-s
                rr = sumli[-1]-s - (l-i-1)*n
                # r = rl+rr
                # print(li,sumli,i,rl,rr,r)
                res[n]=rl+rr
        return res

    def getDistances_t(self, arr: List[int]) -> List[int]:
        num_idli = defaultdict(list)
        for id,num in enumerate(arr):
            num_idli[num].append(id)
        res = []
        for id,num in enumerate(arr):
            r = sum(abs(a-id) for a in num_idli[num])
            res.append(r)
        return res

    def getDistancesw(self, arr: List[int]) -> List[int]:
        cnt_dict,sumid_dict = defaultdict(int),defaultdict(int)
        for id,num in enumerate(arr):
            cnt_dict[num]+=1
            sumid_dict[num]+=id
        res = []
        for id,num in enumerate(arr):
            r = abs(sumid_dict[num]-cnt_dict[num]*id)
            res.append(r)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getDistances(*data)


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
        [[10,5,10,10]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')