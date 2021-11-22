# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 9:35
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 997. 找到小镇的法官.py
# @Software: PyCharm
# ===================================
"""在一个小镇里，按从 1 到 n 为 n 个人进行编号。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足条件 1 和条件 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示编号为 a 的人信任编号为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的编号。否则，返回 -1。

 

示例 1：

输入：n = 2, trust = [[1,2]]
输出：2
示例 2：

输入：n = 3, trust = [[1,3],[2,3]]
输出：3
示例 3：

输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1
示例 4：

输入：n = 3, trust = [[1,2],[2,3]]
输出：-1
示例 5：

输入：n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
输出：3
 

提示：

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
trust[i] 互不相同
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-town-judge
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import numpy as np

from leetcode_python.utils import *

class Solution:
    def __init__(self):
        """
        只有一个点没有出度，有n-1个点有出度
        """
        pass

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0: return 1 if n==1 else -1
        trust_np = np.array(trust)
        set_out = set(trust_np[:,0])
        set_in = set(trust_np[:,1])
        set_only_trusted = set_in - set_out
        if len(set_only_trusted)!=1:    # =0表示没有人只被信任，>1表示存在两个人没信任别人
            return -1
        else:
            maybe = int(set_only_trusted.pop())  # 计算maybe被信任了多少次
            return maybe if len([a for a,b in trust if b==maybe])==n-1 else -1

    def findJudge_(self, n: int, trust: List[List[int]]) -> int:
        set_in,set_out = set(),set(range(1,n+1))
        for a,b in trust:
            if a in set_out: set_out.remove(a)
            set_in.add(b)
        print(set_out,set_in)
        return len(set_out)==1 and set_out[0]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.findJudge(*data)


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
        [2,[[1,2]]],
        [3,[[1,3],[2,3]]],
        [3,[[1,3],[2,3],[3,1]]],
        [3,[[1,2],[2,3]]],
        [4,[[1,3],[1,4],[2,3],[2,4],[4,3]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
