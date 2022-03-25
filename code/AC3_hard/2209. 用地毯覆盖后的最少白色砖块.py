# -*- coding: utf-8 -*-
# @Time    : 2022/3/25 8:38
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 2209. 用地毯覆盖后的最少白色砖块.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。

floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。
floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。
同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。

请你返回没被覆盖的白色砖块的 最少 数目。

 

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
floor[i] 要么是 '0' ，要么是 '1' 。
1 <= numCarpets <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-white-tiles-after-covering-with-carpets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def minimumWhiteTiles(self, floor: str, n: int, carpetLen: int) -> int:
        length = len(floor)
        floor = list(int(x) for x in floor)
        last = [floor[0]]
        for f in floor[1:]: last.append(last[-1] + f)
        while n:
            # print(last)
            now = [0] * (length)
            for j in range(carpetLen, length):
                now[j] = min(now[j - 1] + floor[j], last[j - carpetLen])
            last = now
            n-=1
        # print(last)
        return last[-1]


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.minimumWhiteTiles(*data)

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
        # ["010111110010",2,5],
        ["0111101",1,2],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
