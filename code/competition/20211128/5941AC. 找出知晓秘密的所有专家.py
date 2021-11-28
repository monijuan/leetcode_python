# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 10:29
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5941. 找出知晓秘密的所有专家.py
# @Software: PyCharm
# ===================================
"""给你一个整数 n ，表示有 n 个专家从 0 到 n - 1 编号。另外给你一个下标从 0 开始的二维整数数组 meetings ，其中 meetings[i] = [xi, yi, timei] 表示专家 xi 和专家 yi 在时间 timei 要开一场会。一个专家可以同时参加 多场会议 。最后，给你一个整数 firstPerson 。

专家 0 有一个 秘密 ，最初，他在时间 0 将这个秘密分享给了专家 firstPerson 。接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播。更正式的表达是，每次会议，如果专家 xi 在时间 timei 时知晓这个秘密，那么他将会与专家 yi 分享这个秘密，反之亦然。

秘密共享是 瞬时发生 的。也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享。

在所有会议都结束之后，返回所有知晓这个秘密的专家列表。你可以按 任何顺序 返回答案。



示例 1：

输入：n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
输出：[0,1,2,3,5]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 5 ，专家 1 将秘密与专家 2 共享。
时间 8 ，专家 2 将秘密与专家 3 共享。
时间 10 ，专家 1 将秘密与专家 5 共享。
因此，在所有会议结束后，专家 0、1、2、3 和 5 都将知晓这个秘密。
示例 2：

输入：n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
输出：[0,1,3]
解释：
时间 0 ，专家 0 将秘密与专家 3 共享。
时间 2 ，专家 1 与专家 2 都不知晓这个秘密。
时间 3 ，专家 3 将秘密与专家 0 和专家 1 共享。
因此，在所有会议结束后，专家 0、1 和 3 都将知晓这个秘密。
示例 3：

输入：n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
输出：[0,1,2,3,4]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 1 ，专家 1 将秘密与专家 2 共享，专家 2 将秘密与专家 3 共享。
注意，专家 2 可以在收到秘密的同一时间分享此秘密。
时间 2 ，专家 3 将秘密与专家 4 共享。
因此，在所有会议结束后，专家 0、1、2、3 和 4 都将知晓这个秘密。
示例 4：

输入：n = 6, meetings = [[0,2,1],[1,3,1],[4,5,1]], firstPerson = 1
输出：[0,1,2,3]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 1 ，专家 0 将秘密与专家 2 共享，专家 1 将秘密与专家 3 共享。
因此，在所有会议结束后，专家 0、1、2 和 3 都将知晓这个秘密。


提示：

2 <= n <= 105
1 <= meetings.length <= 105
meetings[i].length == 3
0 <= xi, yi <= n - 1
xi != yi
1 <= timei <= 105
1 <= firstPerson <= n - 1
"""

from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetdict = {}
        for a,b,time in meetings:
            meetdict[a] = meetdict.get(a,list())+[(b,time)]
            meetdict[b] = meetdict.get(b,list())+[(a,time)]
        res = [0,firstPerson]
        queue = [(0,0),(firstPerson,0)] # id,time
        know_time = [-1 for _ in range(n)]
        know_time[0]=0
        know_time[firstPerson]=0
        while queue:
            nowid,time_know = queue.pop(0)
            nextlist = meetdict.get(nowid,list()).copy()
            for nextid,time_meet in nextlist:
                if time_meet>=time_know:# 知道后的meet
                    meetdict[nowid].remove((nextid,time_meet))
                    if know_time[nextid]==-1:#第一次知道
                        res.append(nextid)
                        know_time[nextid]=time_meet
                        queue.append((nextid,time_meet))
                    elif know_time[nextid]>time_meet:#其实更早就知道了
                        know_time[nextid]=time_meet
                        queue.append((nextid,time_meet))
        return res


    def findAllPeople_(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetdict = {}
        for a,b,time in meetings:
            meetdict[a] = meetdict.get(a,list())+[(b,time)]
            meetdict[b] = meetdict.get(b,list())+[(a,time)]
        res = [0,firstPerson]
        queue = [(0,0),(firstPerson,0)] # id,time
        know_time = [-1 for _ in range(n)]
        know_time[0]=0
        know_time[firstPerson]=0
        while queue:
            nowid,time_know = queue.pop(0)
            print('nowid',nowid,time_know)
            for nextid,time_meet in meetdict.get(nowid,list()):
                if time_meet>=time_know:
                    print('before',nowid,'-',nextid,meetdict[nowid])
                    meetdict[nowid].remove((nextid,time_meet))
                    print('after',nowid,'-',nextid,meetdict[nowid])
                    if know_time[nextid]==-1 or nextid not in res: # 第一次知道
                        queue.append((nextid,time_meet))
                        print('append',nextid)
                        res.append(nextid)
                        know_time[nextid] = time_meet
                    elif know_time[nextid]>time_meet:# 发现更早就知道了
                        queue.append((nextid, time_meet))
                        know_time[nextid] = time_meet
        return res


    def findAllPeople_超时(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetdict = {}
        for a,b,time in meetings:
            meetdict[a] = meetdict.get(a,list())+[(b,time)]
            meetdict[b] = meetdict.get(b,list())+[(a,time)]
        res = [0,firstPerson]
        queue = [(0,0),(firstPerson,0)] # id,time
        mintime = {firstPerson:0,0:0}
        # for k,v in meetdict.items():
        #     print(k,v)
        while queue:
            nowid,time_know = queue.pop(0)
            # print('now',nowid,time_know)
            for nextid,time_meet in meetdict.get(nowid,list()):
                # print('next',nextid,time_meet,end=' -->')
                if time_meet>=time_know and time_meet<mintime.get(nextid,float('inf')):
                    # print('append',nextid,end='')
                    if nextid not in res: res.append(nextid)
                    queue.append((nextid,time_meet))
                    mintime[nextid] = time_meet
                # print()
        return res


    def findAllPeople_没考虑先后知道(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetdict = {}
        for a,b,time in meetings:
            meetdict[a] = meetdict.get(a,list())+[(b,time)]
            meetdict[b] = meetdict.get(b,list())+[(a,time)]
        res = [0,firstPerson]
        queue = [(0,0),(firstPerson,0)] # id,time
        for k,v in meetdict.items():
            print(k,v)
        while queue:
            nowid,time_know = queue.pop(0)
            print('now',nowid,time_know)
            for nextid,time_meet in meetdict.get(nowid,list()):
                print('next',nextid,time_meet,end=' -->')
                if nextid not in res and time_meet>=time_know:
                    print('append',nextid,end='')
                    res.append(nextid)
                    queue.append((nextid,time_meet))
                print()
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.findAllPeople(*data)


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
        # [6,[[1,2,5],[2,3,8],[1,5,10]],1],
        [12,[[10,8,6],[9,5,11],[0,5,18],[4,5,13],[11,6,17],[0,11,10],[10,11,7],[5,8,3],[7,6,16],[3,6,10],[3,11,1],[8,3,2],[5,0,7],[3,8,20],[11,0,20],[8,3,4],[1,9,4],[10,7,11],[8,10,18]],9],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
