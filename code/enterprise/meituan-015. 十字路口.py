# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 11:38
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-015. 十字路口.py
# @Software: PyCharm
# ===================================
"""在小美和小团生活的城市中，有 n 行 m 列共计 n * m 个十字路口，第 i 行 j 列的十字路口有两个属性 a[i][j]，b[i][j] 。当行人处在 i 行 j 列的路口，对于任意非负整数 k :
当时间处在 [k * a[i][j] + k * b[i][j], (k+1) * a[i][j] + k * b[i][j])时，行人可以选择走到 i±1 行 j 列的路口。
当时间处在 [(k+1) * a[i][j] + k * b[i][j], (k+1) * a[i][j] + (k+1) * b[i][j])时，行人可以选择走到 i 行 j±1 列的路口。
每次移动花费的时间为 1 ，且要保证将要去的十字路口存在，即属于 n * m 个路口当中。可以选择原地静止不动。
在第 0 时刻，小美处在 xs 行 ys 列的十字路口处，要去 xt 行 yt 列的十字路口找小团。小团原地不动等小美，请问小美所花费的时间最少是多少?

格式：


输入：
- 第一行六个正整数 n,m,xs,ys,xt,yt ，含义如上文所示。以样例第一行【5、5、2、4、4、3】 共计 6 个数字为例：
  - 前两位数字代表有 5*5 的二维数组
  - 三、四位数字代表小美处在 2 行 4 列的十字路口处
  - 五、六位数字代表要去 4 行 3 列的十字路口找小团。
- 接下来 n 行每行 m 个正整数，在样例中为第一个 5*5 的二维数组，第 i 行第 j 个数代表 i 行 j 列十字路口的属性 a[i][j] 。
- 接下来 n 行每行 m 个正整数，在样例中为第二个 5*5 的二维数组，第 i 行第 j 个数代表 i 行 j 列十字路口的属性 b[i][j]。
输出：
- 输出 1 行 1 个整数代表答案。
示例：


输入：
     5 5 2 4 4 3
     2 1 1 3 1
     1 4 2 3 1
     4 4 4 2 1
     3 1 1 2 4
     5 1 5 5 1
     5 3 4 1 3
     1 1 2 2 2
     2 1 4 4 5
     1 1 5 3 3
     3 2 1 3 3
输出：3
提示：

对于100%的数据，1 ≤ n, m, xs, ys, xt, yt, a[i][j], b[i][j] ≤ 100
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/KLwc3e
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

n, m, xs, ys, xt, yt = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

import heapq

queue = [(0, xs - 1, ys - 1)]
time = {(xs - 1, ys - 1): 0}

while queue:
    t, x, y = heapq.heappop(queue)
    if t % (a[x][y] + b[x][y]) < a[x][y]:
        if x + 1 < n and ((x + 1, y) not in time or time[(x + 1, y)] > t + 1):
            time[(x + 1, y)] = t + 1
            heapq.heappush(queue, [t + 1, x + 1, y])

        if x - 1 >= 0 and ((x - 1, y) not in time or time[(x - 1, y)] > t + 1):
            time[(x - 1, y)] = t + 1
            heapq.heappush(queue, [t + 1, x - 1, y])

    elif b[x][y] + a[x][y] > t % (a[x][y] + b[x][y]) >= a[x][y]:
        if y + 1 < m and ((x, y + 1) not in time or time[(x, y + 1)] > t + 1):
            time[(x, y + 1)] = t + 1
            heapq.heappush(queue, [t + 1, x, y + 1])

        if y - 1 >= 0 and ((x, y - 1) not in time or time[(x, y - 1)] > t + 1):
            time[(x, y - 1)] = t + 1
            heapq.heappush(queue, [t + 1, x, y - 1])

    cur = t % (a[x][y] + b[x][y])
    if cur < a[x][y]:
        cost = a[x][y] - cur + 1
        if y + 1 < m and ((x, y + 1) not in time or time[(x, y + 1)] > cost + t):
            time[(x, y + 1)] = cost + t
            heapq.heappush(queue, [cost + t, x, y + 1])
        if y - 1 >= 0 and ((x, y - 1) not in time or time[(x, y - 1)] > cost + t):
            time[(x, y - 1)] = cost + t
            heapq.heappush(queue, [cost + t, x, y - 1])

    elif cur < a[x][y] + b[x][y]:
        cost = a[x][y] + b[x][y] - cur + 1
        if x + 1 < n and ((x + 1, y) not in time or time[(x + 1, y)] > cost + t):
            time[(x + 1, y)] = cost + t
            heapq.heappush(queue, [cost + t, x + 1, y])

        if x - 1 >= 0 and ((x - 1, y) not in time or time[(x - 1, y)] > cost + t):
            time[(x - 1, y)] = cost + t
            heapq.heappush(queue, [cost + t, x - 1, y])

print(time[(xt - 1, yt - 1)])
