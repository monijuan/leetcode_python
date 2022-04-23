# -*- coding: utf-8 -*-
# @Time    : 2022/4/23 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 587. 安装栅栏.py
# @Software: PyCharm 
# ===================================
"""在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

 

示例 1:

输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:

示例 2:

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
解释:

即使树都在一条直线上，你也需要先用绳子包围它们。
 

注意:

所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
输入的整数在 0 到 100 之间。
花园至少有一棵树。
所有树的坐标都是不同的。
输入的点没有顺序。输出顺序也没有要求。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/erect-the-fence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # 斜率公式换算为乘积
        def sign(p, q, r):
            return (p[0] - r[0]) * (q[1] - r[1]) - (p[1] - r[1]) * (q[0] - r[0])

        # 判断添加点 r 是否在前面两点连线的右边
        def check_valid(points, r):
            points.append(r)
            while len(points) >= 3 and sign(*points[-3:]) < 0:
                points.pop(-2)
            return points

        trees.sort(key=lambda p: (p[0], p[1]))
        lower = reduce(check_valid, trees, [])
        upper = reduce(check_valid, trees[::-1], [])
        return lower + list(filter(lambda p: p not in lower, upper))


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.outerTrees(*data)

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
        [[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
