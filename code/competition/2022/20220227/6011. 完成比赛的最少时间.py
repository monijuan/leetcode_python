# -*- coding: utf-8 -*-
# @Time    : 2022/2/27 9:18
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6011. 完成比赛的最少时间.py
# @Software: PyCharm 
# ===================================
"""给你一个数组 time ，其中 time[i] 表示第 i 辆公交车完成 一趟旅途 所需要花费的时间。

每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。

给你一个整数 totalTrips ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 totalTrips 趟旅途需要花费的 最少 时间。



示例 1：

输入：time = [1,2,3], totalTrips = 5
输出：3
解释：
- 时刻 t = 1 ，每辆公交车完成的旅途数分别为 [1,0,0] 。
  已完成的总旅途数为 1 + 0 + 0 = 1 。
- 时刻 t = 2 ，每辆公交车完成的旅途数分别为 [2,1,0] 。
  已完成的总旅途数为 2 + 1 + 0 = 3 。
- 时刻 t = 3 ，每辆公交车完成的旅途数分别为 [3,1,1] 。
  已完成的总旅途数为 3 + 1 + 1 = 5 。
所以总共完成至少 5 趟旅途的最少时间为 3 。
示例 2：

输入：time = [2], totalTrips = 1
输出：2
解释：
只有一辆公交车，它将在时刻 t = 2 完成第一趟旅途。
所以完成 1 趟旅途的最少时间为 2 。


提示：

1 <= time.length <= 105
1 <= time[i], totalTrips <= 107
"""
from leetcode_python.utils import *

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        LARGE = 10 ** 18
        MINLARGE = 10 ** 12
        min_block = [10 ** 18 for _ in range(20)]
        for a, b in tires:
            val = 0
            for i in range(20):
                val += a * pow(b, i)
                min_block[i] = min(min_block[i], val)
                if val > MINLARGE:
                    break
        dp = [LARGE for _ in range(numLaps + 1)]
        dp[0] = 0
        for i in range(1, numLaps + 1):
            for j in range(1, 20):
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i - j] + min_block[j - 1] + changeTime)
        return dp[-1] - changeTime

import math
class Solution2:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        print(changeTime,numLaps)
        frsn = {}
        tires.sort(key=lambda p:[p[0],p[1]])
        # print(tires)
        lastf = -1
        for f,r in tires:
            if f==lastf:continue
            n = math.ceil(math.log(1+changeTime/f,r))
            s = f * (1-r**n) // (1-r)
            if n not in frsn or frsn[n][2]>s: frsn[n] = [f,r,s,n]
            lastf = f
        print(frsn)
        res = 0
        for f,r,s,n in sorted(frsn.values(),key=lambda p:-p[3]):
            if numLaps==1:break
            if n>numLaps:continue
            loops = numLaps//n
            print(f,r,s,n,numLaps,loops,res)
            numLaps %= n
            res+=s*loops+(loops*changeTime if res else (loops-1)*changeTime)
            print('res:',res)
        print(numLaps)
        if numLaps:
            res+=changeTime+tires[0][0]
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.minimumFinishTime(*data)


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
        # [[[1,10],[2,2],[3,4]],6,5],
        # [[[1,10],[2,2],[3,4],[3,2]],100,5],
        [[[99,7]],85,95], # 17395
        # 138
        # [[[96,6],[13,9],[39,7],[6,5],[94,10],[70,6],[16,5],[65,7],[69,2],[88,7],[75,5],[67,7],[79,3],[7,5],[31,5],[23,3],[40,6],[35,7],[20,5],[76,10],[98,9],[80,2],[2,4],[71,5],[53,8],[87,10],[65,5],[15,4],[32,7],[82,3],[69,5],[58,3],[57,6],[13,7],[98,9],[92,4],[36,3],[82,2],[19,4],[78,3],[90,9],[73,3],[7,4],[81,3],[13,6],[39,3],[74,4]],7,17],
        [[[36,5],[32,5],[88,8],[11,4],[52,2],[2,2],[90,5],[49,6],[68,9],[77,3],[42,7],[17,3],[73,7],[89,2],[92,9],[40,7],[71,8],[79,3],[55,6],[77,9],[14,3],[87,10],[4,2],[63,7],[79,8],[3,9],[44,2],[49,9],[91,3],[58,6],[62,3],[72,7],[97,6],[29,5],[88,9],[40,8],[36,4],[82,8],[53,8],[26,2],[26,6],[92,2],[46,2],[75,6],[85,2],[6,10],[12,4],[15,4]],24,27],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

