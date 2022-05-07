# -*- coding: utf-8 -*-
# @Time    : 2022/5/7 17:18
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1901. 找出顶峰元素 II.py
# @Software: PyCharm 
# ===================================
"""一个 2D 网格中的 顶峰元素 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。

给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 顶峰元素 mat[i][j] 并 返回其位置 [i,j] 。

你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。

要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法

 

 

示例 1:



输入: mat = [[1,4],[3,2]]
输出: [0,1]
解释: 3和4都是顶峰元素，所以[1,0]和[0,1]都是可接受的答案。
示例 2:



输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
输出: [1,1]
解释: 30和32都是顶峰元素，所以[1,1]和[2,2]都是可接受的答案。
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
任意两个相邻元素均不相等.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-a-peak-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l, r = 0, len(mat) - 1
        while l <= r:
            m = (l + r) >> 1
            localMax = max(mat[m])  # 一行最大
            localCol = mat[m].index(localMax)
            if m + 1 < len(mat) and mat[m + 1][localCol] > localMax:
                l = m + 1
            elif m - 1 >= 0 and mat[m - 1][localCol] > localMax:
                r = m - 1
            else:
                return [m, localCol]


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
