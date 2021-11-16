# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 15:31
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 15. 游乐园的迷宫.py
# @Software: PyCharm
# ===================================
"""小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。每两点之间有一条直线相连。游戏没有规定起点和终点，但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。访问的顺序需要满足一串给定的长度为 N-2 由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。根据这个提示，小王希望你能够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。



（上图：A->B->C 右转； 下图：D->E->F 左转）

示例 1：

输入：points = [[1,1],[1,4],[3,2],[2,1]], direction = "LL"

输入：[0,2,1,3]

解释：[0,2,1,3] 是符合"LL"的方案之一。在 [0,2,1,3] 方案中，0->2->1 是左转方向， 2->1->3 也是左转方向

示例 2：

输入：points = [[1,3],[2,4],[3,3],[2,1]], direction = "LR"

输入：[0,3,1,2]

解释：[0,3,1,2] 是符合"LR"的方案之一。在 [0,3,1,2] 方案中，0->3->1 是左转方向， 3->1->2 是右转方向

限制：

3 <= points.length <= 1000 且 points[i].length == 2
1 <= points[i][0],points[i][1] <= 10000
direction.length == points.length - 2
direction 只包含 "L","R"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/you-le-yuan-de-mi-gong
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def getVector(self, a, b):
        """
        :param a: a点坐标id
        :param b: b点坐标id
        :return: 向量 ab
        """
        a, b = self.points[a],self.points[b]
        return [b[0] - a[0], b[1] - a[1]]

    def getCross(self, v1, v2):
        """
        :param v1: 向量v1
        :param v2: 向量v2
        :return: v1和v2矢量积
        """
        return v1[0] * v2[1] - v1[1] * v2[0]

    def getCrossABCD(self,a,b,c,d):
        """
        :param a: a点坐标id
        :param b: b点坐标id
        :param c: c点坐标id
        :param d: d点坐标id
        :return: 向量ab 和 向量cd 的矢量积
        """
        return self.getCross(self.getVector(a,b),self.getVector(c,d))

    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        self.points = points
        length = len(points)
        flag = [0]*length
        res = []
        now_id = 0
        for id,point in enumerate(points):
            if point[0]<points[now_id][0]:
                now_id=id
        flag[now_id]=1
        res.append(now_id)
        
        for dir in direction:
            next_id = -1
            if dir=='L':
                for id in range(length):
                    if 0==flag[id] and (-1==next_id or self.getCrossABCD(now_id,id,now_id,next_id)>0):
                        next_id = id
            else:
                for id in range(length):
                    if 0==flag[id] and (-1==next_id or self.getCrossABCD(now_id,id,now_id,next_id)<0):
                        next_id = id
            flag[next_id]=1
            res.append(next_id)
            now_id = next_id
        res.append(flag.index(0))
        return res


def test(data_test):
    s = Solution()
    return s.visitOrder(*data_test)


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
        [[[3,5],[4,5],[9,1],[5,6],[4,2]],"RLR"],        # [0,3,1,2,4]
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
