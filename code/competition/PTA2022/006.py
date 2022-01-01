# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 23:49
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 001.py
# @Software: PyCharm 
# ===================================
"""
"""
class Solution:
    def oneSide2Highest(self,height):
        resh, resw = 0, 0
        highest = 0
        stack = []
        for now in height:
            if now<highest:
                stack.append(now)
            else:
                w=0
                for h in stack:
                    w+=1
                    resh = max(resh, min(now,highest)-h)
                resw+=1
                stack = [now]   # 注意，这个最高点之后还会用到
                highest = now
        return resh,resw,stack

    def trap(self, height):
        resh1,resw1,stack = self.oneSide2Highest(height)   # 从左往右
        resh2,resw2,stack = self.oneSide2Highest(stack[::-1])  # 此时如果stack还有数，说明 highest 在中间，右边的数换个方向再来一遍
        return max(resh1,resh2),max(resw1,resw2)

n = input()
nums = map(int,input().split())
s = Solution()
resh1,resw1 = s.trap(nums)

print(resw1)
print(resh1)




