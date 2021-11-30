# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 9:15
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-005. 小美的区域会议.py
# @Software: PyCharm
# ===================================
"""
"""

### 测试case
""" # 27
10 1
1 2
2 3
3 4
4 5
6 7
7 8
8 9
9 10
10 6
2 2 2 2 2  2 2 2 3 4
"""

""" # 49
15 1
1 2
2 3
3 4
4 5
6 7
7 8
8 9
9 10
10 6
11 5
12 11
13 12
13 2
5 12
2 2 3 5 4 2 2 2 3 4 3 3 2 2 1
"""


def wrong():

    num,k = list(map(int,input().split()))
    nexts = [[] for _ in range(num+1)]
    for _ in range(num-1):
        a,b = list(map(int,input().split()))
        nexts[a].append(b)
        nexts[b].append(a)
    grades = [0]+list(map(int,input().split()))

    res = 0
    mod = 10**9+7
    visited = [0]*(num+1)

    def dfs(now,min_grade,max_grade,show=True):
        if not min_grade<=grades[now]<=max_grade:
            return 0
        visited[now] = 1
        cnt = 1
        for next in nexts[now]:
            if 0==visited[next] and now<next:
                cnt*=(1+dfs(next,min_grade,max_grade,show=show))
                cnt%=mod
        visited[now] = 0
        return cnt

    for start in range(1,num+1):
        print(start,dfs(start,grades[start],grades[start]+k))
        res+=dfs(start,start,grades[start],grades[start]+k)
        res%=mod
    print(res)

def ac():
    import collections
    MOD = 10 ** 9 + 7
    n, k = map(int, input().split())
    adjvex = collections.defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1  # 结点ID号统一成从0开始
        y -= 1
        adjvex[x].append(y)
        adjvex[y].append(x)
    rank = [int(x) for x in input().split()]
    min_rank = -1
    max_rank = -1
    root = -1  # 回溯时的基准root结点，方便比较，防止重复
    def backtrace(x: int) -> int:
        if not (min_rank <= rank[x] <= max_rank):
            return 0
        if x < root:
            return 0
        cnt = 1
        visited[x] = True
        for y in adjvex[x]:
            if visited[y] == False:
                cnt = cnt * (backtrace(y) + 1) % MOD
        visited[x] = False
        return cnt

    visited = [False for _ in range(n)]
    res = 0
    for x in range(n):
        visited[x] = True
        min_rank = rank[x]  # 最低的级别
        max_rank = rank[x] + k  # 最高的级别
        root = x  # 标记，防止重复
        backtrace_x = backtrace(x)
        print(x+1,backtrace_x)
        res += backtrace_x
        res %= MOD
        visited[x] = False
    print(res)




