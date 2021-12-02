# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 9:56
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-010. 小团的默契游戏.py
# @Software: PyCharm
# ===================================
"""小团从某不知名论坛上突然得到了一个测试默契度的游戏，想和小美玩一次来检验两人的默契程度。游戏规则十分简单，首先给出一个长度为 n 的序列，最大值不超过 m 。
小团和小美各自选择一个 [1,m] 之间的整数，设小美选择的是 l ，小团选择的是 r ，我们认为两个人是默契的需要满足以下条件:

l 小于等于 r 。
对于序列中的元素 x ，如果 0<x<l ，或 r<x<m+1 ,则 x 按其顺序保留下来，要求保留下来的子序列单调不下降。
小团为了表现出与小美最大的默契，因此事先做了功课，他想知道能够使得两人默契的二元组 <l,r> 一共有多少种。
我们称一个序列 A 为单调不下降的，当且仅当对于任意的 i>j ，满足 A[i]>=A[j] 。

格式：


输入：
- 输入第一行包含两个正整数 m 和 n ，表示序列元素的最大值和序列的长度。
- 输入第二行包含 n 个正整数，表示该序列。
输出：
- 输出仅包含一个整数，表示能使得两人默契的二元组数量。
示例：


输入：
     5 5
     4 1 4 1 2
输出：10
提示：

1 <= n, m <= 100000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yqj8Su
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


###测试case
# m, length = 10,20
# nums =[10, 8, 10, 8, 8, 3, 3, 6, 3, 5, 5, 2, 8, 3, 7, 9, 5, 9, 9, 9]

###测试case
# m, length = 5,5
# nums =[4,1,4,1,2]
# 应该有这10对：
#
# 1 2 剩下序列 44
# 1 3 剩下序列 44
# 1 4 剩下序列 (空)
# 1 5 剩下序列 (空)
# 2 4 剩下序列 11
# 2 5 剩下序列 11
# 3 4 剩下序列 112
# 3 5 剩下序列 112
# 4 4 剩下序列 112
# 4 5 剩下序列 112


m, length = list(map(int, input().split()))
nums = list(map(int, input().split()))
def judge(l, r):
    _min = 0
    for x in nums:
        if l <= x <= r: continue
        if x < _min: return False
        _min = x
    return True

def getR(left):
    l, r = left, length
    while l <= r:
        mid = (l + r) >> 1
        if judge(left, mid): r = mid - 1
        else: l = mid + 1
    return l

res = 0
for left in range(1, m + 1):
    right = getR(left)
    if right == length + 1: break
    res += length - right + 1   # 因为非递减序列的子序列肯定也是非递减的

print(res)