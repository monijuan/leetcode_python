# -*- coding: utf-8 -*-
# @Time    : 2022/3/11 21:56
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5203AC. 统计可以提取的工件.py
# @Software: PyCharm 
# ===================================
"""存在一个 n x n 大小、下标从 0 开始的网格，网格中埋着一些工件。给你一个整数 n 和一个下标从 0 开始的二维整数数组 artifacts ，artifacts 描述了矩形工件的位置，其中 artifacts[i] = [r1i, c1i, r2i, c2i] 表示第 i 个工件在子网格中的填埋情况：

(r1i, c1i) 是第 i 个工件 左上 单元格的坐标，且
(r2i, c2i) 是第 i 个工件 右下 单元格的坐标。
你将会挖掘网格中的一些单元格，并清除其中的填埋物。如果单元格中埋着工件的一部分，那么该工件这一部分将会裸露出来。如果一个工件的所有部分都都裸露出来，你就可以提取该工件。

给你一个下标从 0 开始的二维整数数组 dig ，其中 dig[i] = [ri, ci] 表示你将会挖掘单元格 (ri, ci) ，返回你可以提取的工件数目。

生成的测试用例满足：

不存在重叠的两个工件。
每个工件最多只覆盖 4 个单元格。
dig 中的元素互不相同。


示例 1：


输入：n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
输出：1
解释：
不同颜色表示不同的工件。挖掘的单元格用 'D' 在网格中进行标记。
有 1 个工件可以提取，即红色工件。
蓝色工件在单元格 (1,1) 的部分尚未裸露出来，所以无法提取该工件。
因此，返回 1 。
示例 2：


输入：n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
输出：2
解释：红色工件和蓝色工件的所有部分都裸露出来（用 'D' 标记），都可以提取。因此，返回 2 。


提示：

1 <= n <= 1000
1 <= artifacts.length, dig.length <= min(n2, 105)
artifacts[i].length == 4
dig[i].length == 2
0 <= r1i, c1i, r2i, c2i, ri, ci <= n - 1
r1i <= r2i
c1i <= c2i
不存在重叠的两个工件
每个工件 最多 只覆盖 4 个单元格
dig 中的元素互不相同
"""
from leetcode_python.utils import *

import numpy as np
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        map = [[0]*n for _ in range(n)]
        for r,c in dig:
            map[r][c]=1
        res = 0
        # for r in map:print(r)
        map=np.array(map)
        for r1,c1,r2,c2 in artifacts:
            if np.sum(map[r1:r2+1,c1:c2+1])==(c2-c1+1)*(r2-r1+1):res+=1
        return res



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.digArtifacts(*data)


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
        [6,[[0,2,0,5],[0,1,1,1],[3,0,3,3],[4,4,4,4],[2,1,2,4]],[[0,2],[0,3],[0,4],[2,0],[2,1],[2,2],[2,5],[3,0],[3,1],[3,3],[3,4],[4,0],[4,3],[4,5],[5,0],[5,1],[5,2],[5,4],[5,5]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

