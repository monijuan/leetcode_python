# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 14:57
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 2AC. 烹饪料理.py
# @Software: PyCharm 
# ===================================
"""欢迎各位勇者来到力扣城，城内设有烹饪锅供勇者制作料理，为自己恢复状态。

勇者背包内共有编号为 0 ~ 4 的五种食材，其中 meterials[j] 表示第 j 种食材的数量。通过这些食材可以制作若干料理，cookbooks[i][j] 表示制作第 i 种料理需要第 j 种食材的数量，而 attribute[i] = [x,y] 表示第 i 道料理的美味度 x 和饱腹感 y。

在饱腹感不小于 limit 的情况下，请返回勇者可获得的最大美味度。如果无法满足饱腹感要求，则返回 -1。

注意：

每种料理只能制作一次。
示例 1：

输入：meterials = [3,2,4,1,2]
cookbooks = [[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]]
attribute = [[3,2],[2,4],[7,6]]
limit = 5

输出：7

解释：
食材数量可以满足以下两种方案：
方案一：制作料理 0 和料理 1，可获得饱腹感 2+4、美味度 3+2
方案二：仅制作料理 2， 可饱腹感为 6、美味度为 7
因此在满足饱腹感的要求下，可获得最高美味度 7

示例 2：

输入：meterials = [10,10,10,10,10]
cookbooks = [[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]]
attribute = [[5,5],[6,6],[10,10]]
limit = 1

输出：11

解释：通过制作料理 0 和 1，可满足饱腹感，并获得最高美味度 11

提示：

meterials.length == 5
1 <= cookbooks.length == attribute.length <= 8
cookbooks[i].length == 5
attribute[i].length == 2
0 <= meterials[i], cookbooks[i][j], attribute[i][j] <= 20
1 <= limit <= 100
"""
from leetcode_python.utils import *

class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]], limit: int) -> int:
        if len(cookbooks)==0:return -1 if limit>0 else 0
        max_美味度 = -1
        times = min(m//c if c>0 else 10000 for m,c in zip(materials,cookbooks[0]))
        for i in range(min(2,times+1)):
            meiwei = attribute[0][0]*i
            baofu = attribute[0][1]*i
            res = self.perfectMenu([m-b*i for m,b in zip(materials,cookbooks[0])],
                                   cookbooks[1:],attribute[1:],limit-baofu)
            if res!=-1:
                meiwei+=res
                max_美味度 = max(max_美味度, meiwei)
        return max_美味度



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.perfectMenu(*data)

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
        # [[3,2,4,1,2],[[1,1,0,1,2],[2,1,4,0,0],[3,2,4,1,0]],[[3,2],[2,4],[7,6]],5],
        [[10,10,10,10,10],[[1,1,1,1,1],[3,3,3,3,3],[10,10,10,10,10]],[[5,5],[6,6],[10,10]],1],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
