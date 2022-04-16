# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 14:57
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5. 夺回据点.py
# @Software: PyCharm 
# ===================================
"""欢迎各位勇者来到力扣城，本次试炼主题为「夺回据点」。

魔物了占领若干据点，这些据点被若干条道路相连接，roads[i] = [x, y] 表示编号 x、y 的两个据点通过一条道路连接。

现在勇者要将按照以下原则将这些据点逐一夺回：

在开始的时候，勇者可以花费资源先夺回一些据点，初始夺回第 j 个据点所需消耗的资源数量为 cost[j]

接下来，勇者在不消耗资源情况下，每次可以夺回一个和「已夺回据点」相连接的魔物据点，并对其进行夺回

注：为了防止魔物暴动，勇者在每一次夺回据点后（包括花费资源夺回据点后），需要保证剩余的所有魔物据点之间是相连通的（不经过「已夺回据点」）。

请返回勇者夺回所有据点需要消耗的最少资源数量。

注意：

输入保证初始所有据点都是连通的，且不存在重边和自环
示例 1：

输入：
cost = [1,2,3,4,5,6]
roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]

输出：6

解释：
勇者消耗资源 6 夺回据点 0 和 4，魔物据点 1、2、3、5 相连通；
第一次夺回据点 1，魔物据点 2、3、5 相连通；
第二次夺回据点 3，魔物据点 2、5 相连通；
第三次夺回据点 2，剩余魔物据点 5；
第四次夺回据点 5，无剩余魔物据点；
因此最少需要消耗资源为 6，可占领所有据点。
image.png

示例 2：

输入：
cost = [3,2,1,4]
roads = [[0,2],[2,3],[3,1]]

输出：2

解释：
勇者消耗资源 2 夺回据点 1，魔物据点 0、2、3 相连通；
第一次夺回据点 3，魔物据点 2、0 相连通；
第二次夺回据点 2，剩余魔物据点 0；
第三次夺回据点 0，无剩余魔物据点；
因此最少需要消耗资源为 2，可占领所有据点。
image.png

提示：

1 <= roads.length, cost.length <= 10^5
0 <= roads[i][0], roads[i][1] < cost.length
1 <= cost[i] <= 10^9
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def getResult(self,args):
        return


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
