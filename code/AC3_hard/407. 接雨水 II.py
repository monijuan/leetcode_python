# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 9:06
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 407. 接雨水 II.py
# @Software: PyCharm
# ===================================
"""给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

示例 1:



输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
示例 2:



输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10
 

提示:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

import numpy as np
class Solution:
    def next(self, rowid, colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        self.height,self.width = len(heightMap),len(heightMap[0])
        if self.height<3 and self.width<3:return 0
        maxheight = np.max(heightMap)

        # 恢复最外圈接满水的高度。因为最外圈都不能接水，把不是最高的（也就是不能作围墙的）恢复就行，并且放到队列里进行bfs
        find_less = []
        fullmap = [[maxheight]*self.width for _ in range(self.height)]
        for rowid in range(self.height):
            for colid in range(self.width):
                if (rowid in [0,self.height-1] or colid in [0,self.width-1]) and fullmap[rowid][colid]>heightMap[rowid][colid]:
                    fullmap[rowid][colid] = heightMap[rowid][colid]
                    find_less.append([rowid,colid])

        # 计算所有位置最大接水后的高度，主要从外往里一层层看有没有变小
        while find_less:
            rowid,colid = find_less.pop(0)
            for next_row,next_col in self.next(rowid,colid):
                max_beside = max(heightMap[next_row][next_col],fullmap[rowid][colid])
                if fullmap[next_row][next_col]> max_beside:
                    fullmap[next_row][next_col] = max_beside
                    find_less.append([next_row,next_col])

        # 可以接水量 = 接满水高度 - 原始高度
        return int(np.sum(np.array(fullmap) - np.array(heightMap)))


class Solution_错误:
    def onsSide(self,heights:List[int]):
        res = []
        highest = 0
        stack = []
        for height in heights:
            if height<highest:
                stack.append(height)
            else:
                for h in stack:
                    res.append(min(height,highest)-h)
                stack = [height]   # 注意，这个最高点之后还会用到
                highest = height
        return res,stack

    def 一行最大接水量(self,height_line: List[int]):
        res,stack = self.onsSide(height_line)
        res.extend(self.onsSide(stack[::-1])[0])
        res.append(0)
        return res

    def next(self, rowid, colid):
        res = []
        for row_id, col_id in ((rowid - 1, colid), (rowid, colid - 1), (rowid + 1, colid), (rowid, colid + 1)):
            if 0 <= row_id < self.height and 0 <= col_id < self.width:
                res.append([row_id, col_id])
        return res

    def 求出所有连通域(self):
        pools = []
        while np.max(self.res_map)>0:
            for rowid,row in enumerate(self.res_map):
                for colid,num in enumerate(row):
                    if num>0:
                        pool = [num]
                        queue = [(rowid,colid)]
                        self.res_map[rowid][colid]=0
                        while queue:
                            _rowid,_colid = queue.pop(0)
                            for _r,_c in self.next(_rowid,_colid):
                                _num = self.res_map[_r][_c]
                                if _num>0:
                                    pool.append(_num)
                                    queue.append((_r,_c))
                                    self.res_map[_r][_c]=0
                        pools.append(pool)
        return pools

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import numpy as np
        self.height,self.width = len(heightMap),len(heightMap[0])
        if self.height<3 and self.width<3:return 0

        # 沿着水平方向和竖直方向计算每一个位置的最大接水量
        res_row = np.array([self.一行最大接水量(line) for line in heightMap])
        res_col = np.array([self.一行最大接水量(line) for line in np.array(heightMap).transpose(1,0)]).transpose(1,0)
        self.res_map = np.minimum(res_row,res_col)
        print(np.array(heightMap))
        print(self.res_map)

        # 因为水平方向和竖直方向的接水量不能说明不会溢出，所以要通过计算连通区域的最小值
        # case20：[[5,5,5,1],[5,1,1,5],[5,1,5,5],[5,2,5,8]]
        res = sum([min(pool)*len(pool) for pool in self.求出所有连通域()])

        ### 但其实这也不对，连通区域中虽然有的num很小，但是并不是因为边界不够高，而是因为本身比较高，不能因此受影响
        # 例如例子中的：[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
        return int(res)


def test(data_test):
    s = Solution()
    return s.trapRainWater(*data_test)


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
        [[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]],
        [[[5,5,5,1],[5,1,1,5],[5,1,5,5],[5,2,5,8]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
