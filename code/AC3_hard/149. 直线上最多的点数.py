# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 9:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 149. 直线上最多的点数.py
# @Software: PyCharm
# ===================================
"""给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

 

示例 1：


输入：points = [[1,1],[2,2],[3,3]]
输出：3
示例 2：


输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
 

提示：

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
points 中的所有点 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-points-on-a-line
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        li = []
        for i in range(length):
            di = defaultdict(int)
            di[0]=0
            x1,y1=points[i]
            for j in range(i+1,length):
                x2,y2=points[j]
                if x2==x1: di['0']+=1
                else: di[(y2-y1)/(x2-x1)]+=1
            li.append(max(di.values()))
        return max(li)+1


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
