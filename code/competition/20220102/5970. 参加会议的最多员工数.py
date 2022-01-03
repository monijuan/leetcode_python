# -*- coding: utf-8 -*-
# @Time    : 2022/1/2 10:05
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5970. 参加会议的最多员工数.py
# @Software: PyCharm 
# ===================================
"""一个公司准备组织一场会议，邀请名单上有 n 位员工。公司准备了一张 圆形 的桌子，可以坐下 任意数目 的员工。

员工编号为 0 到 n - 1 。每位员工都有一位 喜欢 的员工，每位员工 当且仅当 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 不会 是他自己。

给你一个下标从 0 开始的整数数组 favorite ，其中 favorite[i] 表示第 i 位员工喜欢的员工。请你返回参加会议的 最多员工数目 。



示例 1：



输入：favorite = [2,2,1,2]
输出：3
解释：
上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
注意，公司也可以邀请员工 1，2 和 3 参加会议。
所以最多参加会议的员工数目为 3 。
示例 2：

输入：favorite = [1,2,0]
输出：3
解释：
每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
座位安排同图 1 所示：
- 员工 0 坐在员工 2 和 1 之间。
- 员工 1 坐在员工 0 和 2 之间。
- 员工 2 坐在员工 1 和 0 之间。
参与会议的最多员工数目为 3 。
示例 3：



输入：favorite = [3,0,1,4,1]
输出：4
解释：
上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
所以公司只能不邀请员工 2 。
参加会议的最多员工数目为 4 。


提示：

n == favorite.length
2 <= n <= 105
0 <= favorite[i] <= n - 1
favorite[i] != i
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findpair(self):
        self.pairs =[]
        for startid in range(self.length):
            next = self.next[startid]
            if next>startid and self.next[next]==startid:
                self.pairs.append((startid,next))

    def findfaved(self,notvis,now):
        res = 0
        li = []
        for next in self.faved[now]:
            if notvis[next]:
                notvis[next]=False
                r,rl = self.findfaved(notvis,next)
                if r+1>res:
                    li = [next] + rl
                    res=r+1
                # notvis[next]=True
        return res,li

    def depth(self,startid):
        now = startid
        last = now
        notvis = [True]*self.length
        notvis[startid]=False
        res = 1
        while notvis[self.next[now]]:
            res+=1
            notvis[now]=False
            last=now
            now = self.next[now]
        if self.next[now] ==startid:
            return res
        elif self.next[now] == last:
            notvis[now] = False
            #还有可能 now <- a <- b的
            r,li = self.findfaved(notvis,now)
            res+=r
            for l in li:notvis[l]=False
            #还可能有 a->b->a的
            res+=2*len([1 for a,b in self.pairs if notvis[a] and notvis[b]])
            return res
        else:return 0

    def maximumInvitations(self, favorite: List[int]) -> int:
        self.next = favorite
        self.length = len(favorite)
        self.faved = defaultdict(list)
        for i,n in  enumerate(favorite):
            self.faved[n].append(i)
        self.findpair()
        res = 0
        for startid in range(self.length):
            print(startid,self.depth(startid))
            res = max(res,self.depth(startid))
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.maximumInvitations(*data)


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
        # [[2,2,1,2]],
        # [[3,0,1,4,1]],
        # [[1,0,0,2,1,4,7,8,9,6,7,10,8]],
        [[7,0,7,13,11,6,8,5,9,8,9,14,15,7,11,6]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')