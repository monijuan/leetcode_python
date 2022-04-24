# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6043AC. 统计包含每个点的矩形数目.py
# @Software: PyCharm 
# ===================================
"""给你一个二维整数数组 rectangles ，其中 rectangles[i] = [li, hi] 表示第 i 个矩形长为 li 高为 hi 。给你一个二维整数数组 points ，其中 points[j] = [xj, yj] 是坐标为 (xj, yj) 的一个点。

第 i 个矩形的 左下角 在 (0, 0) 处，右上角 在 (li, hi) 。

请你返回一个整数数组 count ，长度为 points.length，其中 count[j]是 包含 第 j 个点的矩形数目。

如果 0 <= xj <= li 且 0 <= yj <= hi ，那么我们说第 i 个矩形包含第 j 个点。如果一个点刚好在矩形的 边上 ，这个点也被视为被矩形包含。



示例 1：



输入：rectangles = [[1,2],[2,3],[2,5]], points = [[2,1],[1,4]]
输出：[2,1]
解释：
第一个矩形不包含任何点。
第二个矩形只包含一个点 (2, 1) 。
第三个矩形包含点 (2, 1) 和 (1, 4) 。
包含点 (2, 1) 的矩形数目为 2 。
包含点 (1, 4) 的矩形数目为 1 。
所以，我们返回 [2, 1] 。
示例 2：



输入：rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]
输出：[1,3]
解释：
第一个矩形只包含点 (1, 1) 。
第二个矩形只包含点 (1, 1) 。
第三个矩形包含点 (1, 3) 和 (1, 1) 。
包含点 (1, 3) 的矩形数目为 1 。
包含点 (1, 1) 的矩形数目为 3 。
所以，我们返回 [1, 3] 。


提示：

1 <= rectangles.length, points.length <= 5 * 104
rectangles[i].length == points[j].length == 2
1 <= li, xj <= 109
1 <= hi, yj <= 100
所有 rectangles 互不相同 。
所有 points 互不相同 。
"""
from leetcode_python.utils import *

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles_ys = [[] for _ in range(101)]
        for x,y in rectangles:
            rectangles_ys[y].append([x,y])
        for r in rectangles_ys:
            r.sort(key=lambda r: (r[0], r[1]))

        res = []
        for x,y in points:
            res_ = 0
            for yid in range(101):
                rects = rectangles_ys[yid]
                l,r = 0,len(rects)
                while l<r:
                    m = (l+r)>>1
                    if rects[m][0]<x or rects[m][1]<y:
                        l=m+1
                    else:
                        r = m
                res_+=len(rects)-l
            res.append(res_)
        return res


class Solutionwa:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        maxx = max(r[0] for r in rectangles)+1
        maxy = max(r[1] for r in rectangles)+1
        map = [[0]*maxy for _ in range(maxx)]
        # points.sort(key=lambda p:(p[0],p[1]))
        print(maxx,maxy,map)
        for x,y in points:
            if x<maxx and y<maxy:
                map[x][y] = 1
        for i in range(maxx):
            for j in range(maxy):
                if j:map[i][j]+=map[i][j-1]
                if i:map[i][j]+=map[i-1][j]
        print(map)
        res = [map[i][j] for i,j in rectangles]
        return res



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countRectangles(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        # [[[1,2],[2,3],[2,5]],[[2,1],[1,4]]],
        # [[[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]],[[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]]],
        [[[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]],[[2,3]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
