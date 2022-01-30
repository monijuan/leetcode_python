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
n = 4
kaijiang,caipiao = [2434,
3456,
7888,
1235],[1238,
7878,
2456]

n = int(input())
kaijiang,caipiao = [],[]
for i in range(n):kaijiang.append(str(input()))
for i in range(3):caipiao.append(str(input()))

def cmp(ans,cai):
    ans = str(ans)
    cai = str(cai)
    if ans==cai:return 1
    elif ans[1:]==cai[1:]:return 2
    elif ans[2:]==cai[2:]:return 3
    elif ans[3:]==cai[3:]:return 4
    else:return 5

res = 6
for cai in caipiao:
    for ans in kaijiang:
        res = min(res,cmp(cai,ans))

dic = ['','YiDengJiang!!!','ErDengJiang','SanDengJiang','SiDengJiang','WuDengJiang']

print(dic[res])