# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 10:00
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5932AC. 合法重新排列数对.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的二维整数数组 pairs ，其中 pairs[i] = [starti, endi] 。如果 pairs 的一个重新排列，满足对每一个下标 i （ 1 <= i < pairs.length ）都有 endi-1 == starti ，那么我们就认为这个重新排列是 pairs 的一个 合法重新排列 。

请你返回 任意一个 pairs 的合法重新排列。

注意：数据保证至少存在一个 pairs 的合法重新排列。



示例 1：

输入：pairs = [[5,1],[4,5],[11,9],[9,4]]
输出：[[11,9],[9,4],[4,5],[5,1]]
解释：
输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。
end0 = 9 == 9 = start1
end1 = 4 == 4 = start2
end2 = 5 == 5 = start3
示例 2：

输入：pairs = [[1,3],[3,2],[2,1]]
输出：[[1,3],[3,2],[2,1]]
解释：
输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。
end0 = 3 == 3 = start1
end1 = 2 == 2 = start2
重新排列后的数组 [[2,1],[1,3],[3,2]] 和 [[3,2],[2,1],[1,3]] 都是合法的。
示例 3：

输入：pairs = [[1,2],[1,3],[2,1]]
输出：[[1,2],[2,1],[1,3]]
解释：
输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。
end0 = 2 == 2 = start1
end1 = 1 == 1 = start2


提示：

1 <= pairs.length <= 105
pairs[i].length == 2
0 <= starti, endi <= 109
starti != endi
pairs 中不存在一模一样的数对。
至少 存在 一个合法的 pairs 重新排列。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        length = len(pairs)
        cnt_in,cnt_out = defaultdict(int),defaultdict(int)
        end_dict = defaultdict(list)
        for start,end in pairs:
            cnt_out[start]+=1
            cnt_in[end]+=1
            end_dict[start].append(end)

        # find startid: out>in
        startnum = pairs[0][0]
        for id in cnt_out.keys():
            if cnt_out[id]-cnt_in[id]>0:
                startnum = id
                break

        # dfs
        stack = []
        def dfs(now):
            # stack.append(now) # 不能先插入，例如[[1, 3], [3, 1], [1, 2]]
            while len(end_dict[now]):
                next = end_dict[now].pop(-1)
                dfs(next)
            stack.append(now)   # 必须后插入
        dfs(startnum)
        stack.reverse() # 因为是后插入所以要逆序
        return [[stack[i],stack[i+1]] for i in range(length)]

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.validArrangement(*data)

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
        # [[[5,1],[4,5],[11,9],[9,4]]],
        # [[[1,3],[3,1],[1,2]]],
        [[[1,3],[3,1],[1,2],[2,3],[3,4]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')