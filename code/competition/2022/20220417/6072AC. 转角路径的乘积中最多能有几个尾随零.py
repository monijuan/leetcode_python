# -*- coding: utf-8 -*-
# @Time    : 2022/4/17 10:07
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6072AC. 转角路径的乘积中最多能有几个尾随零.py
# @Software: PyCharm 
# ===================================
"""给你一个二维整数数组 grid ，大小为 m x n，其中每个单元格都含一个正整数。

转角路径 定义为：包含至多一个弯的一组相邻单元。具体而言，路径应该完全 向水平方向 或者 向竖直方向 移动过弯（如果存在弯），而不能访问之前访问过的单元格。在过弯之后，路径应当完全朝 另一个 方向行进：如果之前是向水平方向，那么就应该变为向竖直方向；反之亦然。当然，同样不能访问之前已经访问过的单元格。

一条路径的 乘积 定义为：路径上所有值的乘积。

请你从 grid 中找出一条乘积中尾随零数目最多的转角路径，并返回该路径中尾随零的数目。

注意：

水平 移动是指向左或右移动。
竖直 移动是指向上或下移动。


示例 1：



输入：grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
输出：3
解释：左侧的图展示了一条有效的转角路径。
其乘积为 15 * 20 * 6 * 1 * 10 = 18000 ，共计 3 个尾随零。
可以证明在这条转角路径的乘积中尾随零数目最多。

中间的图不是一条有效的转角路径，因为它有不止一个弯。
右侧的图也不是一条有效的转角路径，因为它需要重复访问已经访问过的单元格。
示例 2：



输入：grid = [[4,3,2],[7,6,1],[8,8,8]]
输出：0
解释：网格如上图所示。
不存在乘积含尾随零的转角路径。


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= grid[i][j] <= 1000
"""

from leetcode_python.utils import *

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def cntx(x,k):
            if x==0:return 0
            res = 0
            while x%k==0:
                x//=k
                res+=1
            return res
        def sumgrid(grid):
            h,w = len(grid),len(grid[0])
            res = [[[0,0]for _ in range(w)] for _ in range(h)]
            for i in range(h):
                for j in range(w):
                    res[i][j][0] = grid[i][j] + (0 if j==0 else res[i][j-1][0])
            for j in range(w):
                for i in range(h):
                    res[i][j][1] = grid[i][j] + (0 if i==0 else res[i-1][j][1])
            return res

        h,w = len(grid),len(grid[0])
        grid2 = [[cntx(grid[i][j],2) for j in range(w)] for i in range(h)]
        grid5 = [[cntx(grid[i][j],5) for j in range(w)] for i in range(h)]
        sumgrid2 = sumgrid(grid2)
        sumgrid5 = sumgrid(grid5)
        res = 0
        for i in range(h):
            for j in range(w):
                r2l = sumgrid2[i][j][0]
                r2r = sumgrid2[i][-1][0]-(sumgrid2[i][j-1][0] if j else 0)
                r5l = sumgrid5[i][j][0]
                r5r = sumgrid5[i][-1][0]-(sumgrid5[i][j-1][0] if j else 0)
                c2u = sumgrid2[i][j][1]
                c2d = sumgrid2[-1][j][1]-(sumgrid2[i-1][j][1] if i else 0)
                c5u = sumgrid5[i][j][1]
                c5d = sumgrid5[-1][j][1]-(sumgrid5[i-1][j][1] if i else 0)
                res = max(
                    res,
                    min(r2l+c2u-grid2[i][j],r5l+c5u-grid5[i][j]),
                    min(r2r+c2u-grid2[i][j],r5r+c5u-grid5[i][j]),
                    min(r2l+c2d-grid2[i][j],r5l+c5d-grid5[i][j]),
                    min(r2r+c2d-grid2[i][j],r5r+c5d-grid5[i][j]),
                )
        return res

def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.maxTrailingZeros(*data)

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
        # [[[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]],
        # [[[899,727,165,249,531,300,542,890],[981,587,565,943,875,498,582,672],[106,902,524,725,699,778,365,220]]],
        [[[961,177,735,299,381,295,714],[52,317,629,876,287,714,416],[707,250,159,17,1000,589,182],[337,365,295,817,263,325,740],[117,290,467,353,272,235,779],[846,10,532,499,655,215,592],[875,107,820,325,797,53,782],[336,32,795,10,718,680,846],[372,49,362,903,851,165,32],[691,486,989,316,429,451,465],[24,607,278,658,591,465,563],[388,828,200,641,831,273,845],[266,46,32,800,556,369,861],[935,652,662,207,524,475,924],[309,928,61,363,999,292,84],[535,930,60,938,493,418,713],[474,77,282,673,491,699,376],[709,787,529,447,259,758,322],[94,547,367,432,610,97,123],[242,387,188,430,797,720,327],[740,818,108,260,284,651,383],[24,284,387,639,828,210,923],[504,606,724,440,30,383,410]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
