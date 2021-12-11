# -*- coding: utf-8 -*-
# @Time    : 2021/12/11 22:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5935. 适合打劫银行的日子.py
# @Software: PyCharm 
# ===================================
"""你和一群强盗准备打劫银行。给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天执勤警卫的数量。日子从 0 开始编号。同时给你一个整数 time 。

如果第 i 天满足以下所有条件，我们称它为一个适合打劫银行的日子：

第 i 天前和后都分别至少有 time 天。
第 i 天前连续 time 天警卫数目都是非递增的。
第 i 天后连续 time 天警卫数目都是非递减的。
更正式的，第 i 天是一个合适打劫银行的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。



示例 1：

输入：security = [5,3,3,3,5,6,2], time = 2
输出：[2,3]
解释：
第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。
示例 2：

输入：security = [1,1,1,1,1], time = 0
输出：[0,1,2,3,4]
解释：
因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。
示例 3：

输入：security = [1,2,3,4,5,6], time = 2
输出：[]
解释：
没有任何一天的前 2 天警卫数目是非递增的。
所以没有适合打劫银行的日子，返回空数组。
示例 4：

输入：security = [1], time = 5
输出：[]
解释：
没有日子前面和后面有 5 天时间。
所以没有适合打劫银行的日子，返回空数组。


提示：

1 <= security.length <= 105
0 <= security[i], time <= 105
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def goodDaysToRobBank_超时2(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        if time==0:return list(range(length))
        elif time*2+1>length:return []
        updown = [0]    # 1递增，-1递减
        for id in range(1,length):
            diff = security[id]-security[id-1]
            if diff>0:updown.append(1)
            elif diff<0:updown.append(-1)
            else:updown.append(0)
        leftnotup = [not 1 in updown[max(0,id-time+1):id+1] for id in range(length)]
        rightnotdown = [not -1 in updown[id+1:min(length,id+time+1)] for id in range(length)]
        res = [id for id in range(time,length-time) if leftnotup[id] and rightnotdown[id] ]
        return res

    def goodDaysToRobBank_超时2(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        if time==0:return list(range(length))
        elif time*2+1>length:return []
        updown = [0]    # 1递增，-1递减
        for id in range(1,length):
            diff = security[id]-security[id-1]
            if diff>0:updown.append(1)
            elif diff<0:updown.append(-1)
            else:updown.append(0)
        leftnotup = [not 1 in updown[max(0,id-time+1):id+1] for id in range(length)]
        rightnotdown = [not -1 in updown[id+1:min(length,id+time+1)] for id in range(length)]
        res = [id for id in range(time,length-time) if leftnotup[id] and rightnotdown[id] ]
        return res

    def goodDaysToRobBank_超时(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        if time==0:return list(range(length))
        if time*2+1>length:return []
        updown = [0]    # 1递增，-1递减
        for id in range(1,length):
            diff = security[id]-security[id-1]
            if diff>0:updown.append(1)
            elif diff<0:updown.append(-1)
            else:updown.append(0)
        res = []

        up = [not 1 in updown[max(0,id-time+1):id] for id in range(length)]
        down = [not -1 in updown[id+1:min(length,id+time+1)] for id in range(length)]
        # print(updown[27:32])

        for id in range(time,length-time):
            # if id==29:
            #     print(id,updown[id-time+1:id],updown[id+1:id+time+1],security[id-1:id+2])
            # if not 1 in updown[id-time+1:id] and not -1 in updown[id+1:id+time+1] and security[id-1]>=security[id]<=security[id+1]:
            if up[id] and down[id] and security[id-1]>=security[id]<=security[id+1]:
                res.append(id)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.goodDaysToRobBank(*data)


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
        # [[1,2,3,4],0],
        # [[1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8],2], ### [5,10,14]
        ### [16,38,58]
        [[77,9,111,138,139,183,112,127,38,123,198,86,163,50,140,106,99,140,152,176,124,181,14,113,53,186,76,165,32,26,137,4,186,193,130,157,173,52,27,101,154,129,34,200,51,184,127,147,197,151,190,95,62,182,77,34,174,162,7,84,105,103,128],2],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')