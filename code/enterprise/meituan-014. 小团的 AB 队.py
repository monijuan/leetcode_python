# -*- coding: utf-8 -*-
# @Time    : 2021/12/1 13:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-014. 小团的 AB 队.py
# @Software: PyCharm
# ===================================
"""小团要组织一只队伍参加 MT 杯竞赛，某媒体赛前要对各参赛队伍实力进行评估，已知这个比赛要求每一个参赛方组织一支由 x 个人组成的 A 队，和 y 个人组成的 B 队，这个媒体在评估时会把 A 队的人员的平均实力值和 B 队人员的平均实力值相加，从而得到一个参赛方的综合实力评估。
小团可选的人手有限，只有 x+y 个人可以供他选择，但是显然不同的人员安排会有不同的综合实力评估，他希望他的综合实力评估尽可能高，请你帮助他完成分队。

格式：


输入：
- 输入第一行包含两个正整数x，y，分别表示 AB 队的人数。
- 输入第二行包含 x+y 个正整数，中间用空格隔开，第i个数字表示第i个人的实力值，每个人的实力值不会超过20000，保证任意两个人都不会有相同的实力值。
输出：
- 输出包含一个长度为 x+y 的字符串，每个字符是 'A'或 'B'，表示某人应该被分在 A 或 B 队。如果存在多种答案，则输出字典序最小的字符串。
示例：


输入：
     4 4
     5 6 4 2 3 8 1 7
输出：AAAABBBB
提示：

1 <= x, y <= 20000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/LMkFuT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random


def 超时():
    x, y = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ave = sum(nums)/(x+y)
    biggerid =[pair[0] for pair in sorted(enumerate(nums),key=lambda pair:-pair[1])[:min(x,y)]] # x个较大的id
    if x<=y:
        res = ['A' if id in biggerid else 'B' for id in range(x + y)]
    else:
        res = ['A' if id not in biggerid else 'B' for id in range(x + y)]
    print(''.join(res))

def ac():
    x, y = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    if x==y:
        res = 'A'*x+'B'*x
    else:
        lessid =set(pair[0] for pair in sorted(enumerate(nums),key=lambda pair:pair[1])[:max(x,y)]) # 较小的id
        if x<y:
            res = ['A' if id not in lessid else 'B' for id in range(x + y)]
        else:
            res = ['A' if id in lessid else 'B' for id in range(x + y)]
    print(''.join(res))