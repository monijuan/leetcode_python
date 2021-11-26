# -*- coding: utf-8 -*-
# @Time    : 2021/11/26 15:31
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 519. 随机翻转矩阵.py
# @Software: PyCharm
# ===================================
"""给你一个 m x n 的二元矩阵 matrix ，且所有值被初始化为 0 。请你设计一个算法，随机选取一个满足 matrix[i][j] == 0 的下标 (i, j) ，并将它的值变为 1 。所有满足 matrix[i][j] == 0 的下标 (i, j) 被选取的概率应当均等。

尽量最少调用内置的随机函数，并且优化时间和空间复杂度。

实现 Solution 类：

Solution(int m, int n) 使用二元矩阵的大小 m 和 n 初始化该对象
int[] flip() 返回一个满足 matrix[i][j] == 0 的随机下标 [i, j] ，并将其对应格子中的值变为 1
void reset() 将矩阵中所有的值重置为 0
 

示例：

输入
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
输出
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

解释
Solution solution = new Solution(3, 1);
solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
 

提示：

1 <= m, n <= 104
每次调用flip 时，矩阵中至少存在一个值为 0 的格子。
最多调用 1000 次 flip 和 reset 方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-flip-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random

from leetcode_python.utils import *

class Solution:
    def __init__(self, m: int, n: int):
        self.n=n
        self.max = m*n-1
        self.selected = set()

    def flip(self) -> List[int]:
        index = random.randint(0,self.max)
        while index in self.selected:
            index = random.randint(0,self.max)
        self.selected.add(index)
        return [index // self.n, index % self.n]

    def reset(self) -> None:
        self.selected = set()

class Solution_超时2:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.remain = list(range(m*n))
        random.shuffle(self.remain)
        self.index = 0

    def flip(self) -> List[int]:
        select = self.remain[self.index]
        self.index+=1
        return [select // self.n, select % self.n]

    def reset(self) -> None:
        self.index = 0

class Solution_超时:
    def __init__(self, m: int, n: int):
        """
        超时case：https://leetcode-cn.com/submissions/detail/242552057/testcase/
        """
        self.m = m
        self.n = n
        self.remain = [id for id in range(m*n)]

    def flip(self) -> List[int]:
        select = random.choice(self.remain)
        self.remain.remove(select)
        return [select // self.n, select % self.n]

    def reset(self) -> None:
        self.remain = [id for id in range(self.m*self.n)]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
        [["Solution","flip","flip","flip","reset","flip"],[[3,1],[],[],[],[],[]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
