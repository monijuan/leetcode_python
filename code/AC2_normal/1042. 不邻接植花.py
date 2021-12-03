# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 9:38
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1042. 不邻接植花.py
# @Software: PyCharm
# ===================================
"""有 n 个花园，按从 1 到 n 标记。另有数组 paths ，其中 paths[i] = [xi, yi] 描述了花园 xi 到花园 yi 的双向路径。在每个花园中，你打算种下四种花之一。

另外，所有花园 最多 有 3 条路径可以进入或离开.

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

以数组形式返回 任一 可行的方案作为答案 answer，其中 answer[i] 为在第 (i+1) 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。

 

示例 1：

输入：n = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
解释：
花园 1 和 2 花的种类不同。
花园 2 和 3 花的种类不同。
花园 3 和 1 花的种类不同。
因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]
示例 2：

输入：n = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]
示例 3：

输入：n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]
 

提示：

1 <= n <= 104
0 <= paths.length <= 2 * 104
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
每个花园 最多 有 3 条路径可以进入或离开

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flower-planting-with-no-adjacent
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        neighbor = defaultdict(list)
        for u, v in paths:
            neighbor[u].append(v)
            neighbor[v].append(u)
        res = [0] * n
        for id in range(1, n + 1):
            colors = set(range(1, 5)) - set(res[v - 1] for v in neighbor[id])
            res[id - 1] = colors.pop()
        return res




def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.gardenNoAdj(*data)


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
        [4,[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
