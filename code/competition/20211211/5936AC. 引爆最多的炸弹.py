# -*- coding: utf-8 -*-
# @Time    : 2021/12/11 22:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5936AC. 引爆最多的炸弹.py
# @Software: PyCharm 
# ===================================
"""5936. 引爆最多的炸弹 显示英文描述
User Accepted:1
User Tried:1
Total Accepted:1
Total Submissions:1
Difficulty:Medium
给你一个炸弹列表。一个炸弹的 爆炸范围 定义为以炸弹为圆心的一个圆。

炸弹用一个下标从 0 开始的二维整数数组 bombs 表示，其中 bombs[i] = [xi, yi, ri] 。xi 和 yi 表示第 i 个炸弹的 X 和 Y 坐标，ri 表示爆炸范围的 半径 。

你需要选择引爆 一个 炸弹。当这个炸弹被引爆时，所有 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。

给你数组 bombs ，请你返回在引爆 一个 炸弹的前提下，最多 能引爆的炸弹数目。



示例 1：



输入：bombs = [[2,1,3],[6,1,4]]
输出：2
解释：
上图展示了 2 个炸弹的位置和爆炸范围。
如果我们引爆左边的炸弹，右边的炸弹不会被影响。
但如果我们引爆右边的炸弹，两个炸弹都会爆炸。
所以最多能引爆的炸弹数目是 max(1, 2) = 2 。
示例 2：



输入：bombs = [[1,1,5],[10,10,5]]
输出：1
解释：
引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。
示例 3：



输入：bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
输出：5
解释：
最佳引爆炸弹为炸弹 0 ，因为：
- 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。
- 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。
- 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。
所以总共有 5 个炸弹被引爆。


提示：

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def isconnect(self,x1,y1,r1,x2,y2,r2):
        # print((x1-x2)**2+(y1-y2)**2,(r1+r2)**2)
        diss2 = (x1-x2)**2+(y1-y2)**2
        return diss2<=r1*r1,diss2<=r2*r2

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        num_c = len(bombs)
        mapdict = defaultdict(list)
        for i,(x1,y1,r1) in enumerate(bombs):
            for j in range(i+1,num_c):
                x2,y2,r2 = bombs[j]
                a2b,b2a = self.isconnect(x1,y1,r1,x2,y2,r2)
                if a2b:
                    mapdict[i].append(j)
                if b2a:
                    mapdict[j].append(i)

        sets = []
        for firstid in range(num_c):
            newset = set()
            flag = [1] * num_c
            flag[firstid] = 0
            queue = [firstid]
            while queue:
                now = queue.pop(0)
                newset.add(now)
                for nextid in mapdict[now]:
                    if flag[nextid]:
                        queue.append(nextid)
                        flag[nextid]=0
            sets.append(newset)
        return max([len(s) for s in sets])


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.maximumDetonation(*data)


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
        # [[[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]],
        # [[[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]]],
        [[[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')