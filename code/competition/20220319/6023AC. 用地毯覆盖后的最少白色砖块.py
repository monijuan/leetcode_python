# -*- coding: utf-8 -*-
# @Time    : 2022/3/19 22:21
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6023AC. 用地毯覆盖后的最少白色砖块.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。

floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。

请你返回没被覆盖的白色砖块的 最少 数目。



示例 1：



输入：floor = "10110101", numCarpets = 2, carpetLen = 2
输出：2
解释：
上图展示了剩余 2 块白色砖块的方案。
没有其他方案可以使未被覆盖的白色砖块少于 2 块。
示例 2：



输入：floor = "11111", numCarpets = 2, carpetLen = 3
输出：0
解释：
上图展示了所有白色砖块都被覆盖的一种方案。
注意，地毯相互之间可以覆盖。


提示：

1 <= carpetLen <= floor.length <= 1000
floor[i] 要么是 '0' ，要么是 '1' 。
1 <= numCarpets <= 1000
"""
from leetcode_python.utils import *


def getres(floor: str, numCarpets: int, carpetLen: int) -> int:
        floor = list(floor)
        lf = len(floor)
        while numCarpets:
            numCarpets-=1
            # 找到可以覆盖最多1的idx
            idx,maxnum = 0,-1
            for i in range(lf-carpetLen+1):
                cnt1 = floor[i:i+carpetLen].count('1')
                if cnt1>maxnum:
                    maxnum=cnt1
                    idx = i
                if maxnum==carpetLen:break
            floor[idx:idx+carpetLen] = ['0' for _ in range(carpetLen)]
        return floor.count('1')

class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        return min(getres(floor,numCarpets,carpetLen), getres(floor[::-1],numCarpets,carpetLen))

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.minimumWhiteTiles(*data)

if __name__ == '__main__':
    datas = [
        # ["10110101",2,2],
        ["10111111",2,4],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

