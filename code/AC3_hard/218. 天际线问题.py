# -*- coding: utf-8 -*-
# @Time    : 2021/11/25 9:23
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 218. 天际线问题.py
# @Software: PyCharm
# ===================================
"""城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

 

示例 1：


输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
示例 2：

输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]
 

提示：

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings 按 lefti 非递减排序

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-skyline-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *
import heapq

class Solution:
    def __init__(self):
        pass

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        info = []
        for left, right, h in buildings:
            info.append([left, -h, right])
            info.append([right, 0, float('inf')])
        info.sort(key=lambda x: (x[0], x[1]))
        que_hights = [[info[0][1], info[0][2]]]
        res = [[info[0][0], -info[0][1]]]
        for i in range(1, len(info)):
            start, _h, end = info[i]
            pre_height = que_hights[0][0]
            while que_hights and start >= que_hights[0][1]: heapq.heappop(que_hights)
            heapq.heappush(que_hights, [_h, end])
            if que_hights[0][0] != pre_height: res.append([start, -que_hights[0][0]])
        return res



    def getSkyline_大佬(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(l, -h, r) for l, r, h in buildings]
        events += [(r, 0, 0) for _, r, _ in buildings]
        events.sort()

        res = [[0, 0]]
        queue = [(0, float('inf'))]
        for l, minusH, r in events:
            h = -minusH
            while l >= queue[0][1]:
                heapq.heappop(queue)
            if h:
                heapq.heappush(queue, (-h, r))
            if res[-1][1] != -queue[0][0]:
                res.append([l, -queue[0][0]])
        return res[1:]

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getSkyline(*data)


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
        # [[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]],   # [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        [[[0,2,3],[2,5,3]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
