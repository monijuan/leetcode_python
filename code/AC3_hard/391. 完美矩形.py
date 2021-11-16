# -*- coding: utf-8 -*-
# @Time    : 2021/11/16 8:58
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 391. 完美矩形.py
# @Software: PyCharm
# ===================================
"""给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 (xi, yi) ，右上顶点是 (ai, bi) 。

如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。

 
示例 1：


输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
输出：true
解释：5 个矩形一起可以精确地覆盖一个矩形区域。
示例 2：


输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
输出：false
解释：两个矩形之间有间隔，无法覆盖成一个矩形。
示例 3：


输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
输出：false
解释：图形顶端留有空缺，无法覆盖成一个矩形。
示例 4：


输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
输出：false
解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
 

提示：

1 <= rectangles.length <= 2 * 104
rectangles[i].length == 4
-105 <= xi, yi, ai, bi <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

import numpy as np
class Solution:
    def __init__(self):
        pass

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        rects_np = np.array(rectangles)
        x_min,y_min = rects_np.min(axis=0)[:2]
        x_max,y_max = rects_np.max(axis=0)[2:]
        outside_points = [
            (x_min,y_min), (x_min,y_max),
            (x_max,y_min), (x_max,y_max),
        ]
        area_all = (x_max-x_min) * (y_max-y_min)
        area_sum = 0
        point_count = {}
        for x1,y1,x2,y2 in rectangles:
            point_count[(x1,y1)] = point_count.get((x1,y1),0) + 1
            point_count[(x2,y2)] = point_count.get((x2,y2),0) + 1
            point_count[(x1,y2)] = point_count.get((x1,y2),0) + 1
            point_count[(x2,y1)] = point_count.get((x2,y1),0) + 1
            area_sum += (x2-x1)*(y2-y1)
        print('area:',area_sum,area_all)
        if area_all!=area_sum:
            return False
        for point,count in point_count.items():
            print(point,count)
            if count==1 and point in outside_points:
                continue
            elif count in [2,4] and point not in outside_points:
                continue
            else:
                return False
            # 不能这样，对于case：[[0,0,4,1],[0,0,4,1]]
            # if count not in [2,4] and point not in outside_points:
            #     return False
        return True


def test(data_test):
    s = Solution()
    return s.isRectangleCover(*data_test)


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
        [[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]],
        [[[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]],
        [[[0,0,4,1],[0,0,4,1]]],
        [[[0,0,3,3],[1,1,2,2],[1,1,2,2]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
