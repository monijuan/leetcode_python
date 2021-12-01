# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 10:19
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-008. 小团无路可逃.py
# @Software: PyCharm
# ===================================
"""小团惹小美生气了，小美要去找小团“讲道理”。小团望风而逃，他们住的地方可以抽象成一棵有n个结点的树，小美位于 x 位置，小团位于 y 位置。小团和小美每个单位时间内都可以选择不动或者向相邻的位置转移，很显然最终小团会无路可逃，只能延缓一下被“讲道理”的时间，请问最多经过多少个单位时间后，小团会被追上。

格式：


输入：
- 输入第一行包含三个整数 n，x，y，分别表示树上的结点数量，小美所在的位置和小团所在的位置。
- 接下来有 n-1 行，每行两个整数 u，v，表示 u 号位置和 v 号位置之间有一条边，即 u 号位置和 v 号位置彼此相邻。
输出：
- 输出仅包含一个整数，表示小美追上小团所需的时间。
示例：


输入：
     5 1 2
     2 1
     3 1
     4 2
     5 3
输出：2
提示：

1 <= n <= 50000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/vSYUMc
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


n,x,y = list(map(int,input().split()))
route_dic = {}
for _ in range(n-1):
    a,b = list(map(int,input().split()))
    route_dic[a] = route_dic.get(a,[]) + [b]
    route_dic[b] = route_dic.get(b,[]) + [a]

# 二者距离
def bfs_time(start):
    time = 0
    time_need = [0]*(n+1)
    vis = [False]*(n+1)
    last_level = [start]
    while last_level:
        next_level = []
        for now in last_level:
            vis[now] = True
            time_need[now] = time
            for next in route_dic[now]:
                if not vis[next]:
                    next_level.append(next)
        last_level = next_level
        time+=1
    return time_need
time_need_x = bfs_time(x)
time_need_y = bfs_time(y)
print(max([0]+[a for a,b in zip(time_need_x,time_need_y) if a>b]))

