# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 10:40
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-003. 小美的跑腿代购.py
# @Software: PyCharm
# ===================================
"""小美的一个兼职是美团的一名跑腿代购员，她有 n 个订单可以接，订单编号是 1~n ，但是因为订单的时效性，他只能选择其中 m 个订单接取，精明的小美当然希望自己总的获利是最大的，已知，一份订单会提供以下信息，跑腿价格 v ，商品重量 w kg，商品每重 1kg ，代购费用要加 2 元，而一份订单可以赚到的钱是跑腿价格和重量加价之和。小美可是开兰博基尼送货的人，所以自然不会在意自己会累这种事情。请问小美应该选择哪些订单，使得自己获得的钱最多。
请你按照选择的订单编号的从小到大顺序，如果存在多种方案，输出订单编号字典序较小的方案。

格式：


输入：
- 输入第一行包含两个正整数 n，m，表示订单的数量和小美可以接的订单数量。
- 接下来有 n 行，第 i 行表示 i-1 号订单的信息。每行有两个正整数 v 和 w  ，表示一个订单的跑腿价格和商品重量。
输出：
- 输出包含 m 个 1~n 之间的正整数，中间用空格隔开，表示选择的订单编号。
示例：


输入：
     5 2
     5 10
     8 9
     1 4
     7 9
     6 10
输出：2 5
提示：

1 <= n, m <= 10000
1 <= v, w <= 1000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/GXV5dX
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

num_order,num_target = map(int,input().split())
orders = []
for id in range(1,num_order+1):
    v,w = map(int,input().split())
    orders.append([id,v+w*2])
res = sorted([x[0] for x in sorted(orders,key=lambda x:(-x[1],x[0]))[:num_target]])
print(' '.join([str(x) for x in res]),end=' ')
