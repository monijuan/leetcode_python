# -*- coding: utf-8 -*-
# @Time    : 2022/4/23 14:58
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 04.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


def checkOneSide(a,b):
    """ 中间互补，两头不同时为0 """
    return all(a_!=b_ for a_,b_ in zip(a[1:-1],b[1:-1])) and '0' in [a[0],b[0]] and '0' in [a[-1],b[-1]]

def checkTwoSide(a,b,c1,c2,fa = False):
    # if fa:a = a[::-1]
    assert c1[-1]==c2[0] ,f"{c1},{c2}"
    return all(a_ != b_ for a_, b_ in zip(a[1:-1], c1[1:-1])) and \
           all(a_ != b_ for a_, b_ in zip(b[1:-1], c2[1:-1])) and \
           [a[-1],b[0],c2[0]].count('1')==1

def checkThreeSide(a,b,c,d1,d2,d3):
    # a = a[::-1]
    # b = b[::-1]
    assert d1[-1]==d2[0] and d2[-1]==d3[0] ,f"{d1,d2,d3}"
    return all(a_ != b_ for a_, b_ in zip(a[1:-1], d1[1:-1])) and \
           all(a_ != b_ for a_, b_ in zip(b[1:-1], d2[1:-1])) and \
           all(a_ != b_ for a_, b_ in zip(c[1:-1], d3[1:-1])) and \
           [a[-1],b[0],d2[0]].count('1')==1 and \
           [b[-1],c[0],d3[0]].count('1')==1

def checkFourSide(a,b,c,d,d1,d2,d3,d4):
    # a=a[::-1]
    # b=b[::-1]
    # c=c[::-1]
    assert d1[-1]==d2[0] and d2[-1]==d3[0] and d3[-1]==d4[0] and d4[-1]==d1[0] ,f"{d1,d2,d3,d4}"
    return all(a_ != b_ for a_, b_ in zip(a[1:-1], d1[1:-1])) and \
           all(a_ != b_ for a_, b_ in zip(b[1:-1], d2[1:-1])) and \
           all(a_ != b_ for a_, b_ in zip(c[1:-1], d3[1:-1])) and \
           all(a_ != b_ for a_, b_ in zip(d[1:-1], d4[1:-1])) and \
           [a[-1],b[0],d2[0]].count('1')==1 and \
           [b[-1],c[0],d3[0]].count('1')==1 and \
           [c[-1],d[0],d4[0]].count('1')==1 and \
           [d[-1],a[0],d1[0]].count('1')==1


def get4edge(shape):
    a = shape[0]               # 边1
    b = ''.join([s[-1] for s in shape]) # 边2
    c = shape[-1][::-1]             # 边3
    d = ''.join([s[0] for s in shape[::-1]])    # 边4
    return a,b,c,d

def flips(a,b,c,d):
    return a[::-1],d[::-1],c[::-1],b[::-1]

def flip(a):
    return a[::-1]


class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
        ###
        for r in zip(*shapes):print('|'.join(x.replace('0',' ').replace('1','o') for x in r))
        ###
        edges = [get4edge(s) for s in shapes]
        # for e in edges:print(e)
        # 确认第一块
        e_a1,e_a2,e_a3,e_a4 = edges[0]

        # 找相邻第二块
        res_2ed = []    # [id2,e_b,ee1,ell]
        for id2 in range(1,6):
            for i_,e2_ in enumerate(edges[id2]):
                if checkOneSide(e_a1,e2_):
                    # es = flips(*edges[id2])
                    # res_2ed.append([id2,es[(i_+1)%4],es[(i_+2)%4],es[(i_+3)%4]])
                    # res_2ed.append([id2,edges[id2][(i_+1)%4],edges[id2][(i_+2)%4],edges[id2][(i_+3)%4]])
                    res_2ed.append([id2,flip(edges[id2][(i_+1)%4]),flip(edges[id2][(i_+2)%4]),flip(edges[id2][(i_+3)%4])])
            edges_id2_f = flips(*edges[id2])
            for i_,e2_ in enumerate(edges_id2_f):
                if checkOneSide(e_a1,e2_):
                    es = edges[id2]
                    # res_2ed.append([id2,es[(i_+1)%4],es[(i_+2)%4],es[(i_+3)%4]])
                    # res_2ed.append([id2,edges_id2_f[(i_+1)%4],edges_id2_f[(i_+2)%4],edges_id2_f[(i_+3)%4]])
                    res_2ed.append([id2,flip(edges_id2_f[(i_+1)%4]),flip(edges_id2_f[(i_+2)%4]),flip(edges_id2_f[(i_+3)%4])])
        # for r in res_2ed:print(r)
        print('len res2',len(res_2ed))

        # 找第3块：
        res_3ed = []
        for id2,e_b,ee1,ell in res_2ed:
            for id3 in range(1,6):
                if id3==id2:continue
                for i_,e3_ in enumerate(edges[id3]):
                    e3_next = edges[id3][(i_+1)%4]
                    # print(id3,edges[id3],i_)
                    if checkTwoSide(e_b,e_a2,e3_,e3_next,fa=True):
                        res_3ed.append([[id2,id3],
                                           flip(edges[id3][(i_+3)%4]),
                                           [ee1,flip(edges[id3][(i_+2)%4])],
                                           ell,
                                       ])
                edges_id3_f = flips(*edges[id3])
                for i_,e3_ in enumerate(edges_id3_f):
                    e3_next = edges_id3_f[(i_+1)%4]
                    if checkTwoSide(e_b,e_a2,e3_,e3_next,fa=True):
                        res_3ed.append([[id2,id3],
                                           # edges_id3_f[(i_+3)%4],
                                           # [ee1,edges_id3_f[(i_+2)%4]],
                                           flip(edges[id3][(i_+3)%4]),
                                           [ee1,flip(edges[id3][(i_+2)%4])],
                                           ell,
                                       ])

        # for r3 in res_3ed:print('r3:',r3)
        print('len res3',len(res_3ed))

        # 找第4块：
        res_4ed = []
        for visited,e_b,last4e,ell in res_3ed:
            for id4 in range(1,6):
                if id4 in visited:continue
                for i_,e4_ in enumerate(edges[id4]):
                    e4_next = edges[id4][(i_+1)%4]
                    if checkTwoSide(e_a3,e_b,e4_,e4_next):
                        res_4ed.append([visited+[id4],
                                           # edges[id4][(i_+3)%4],
                                           # last4e+[edges[id4][(i_+2)%4]],
                                           flip(edges[id4][(i_+3)%4]),
                                           last4e+[flip(edges[id4][(i_+2)%4])],
                                           ell,
                                       ])
                edges_id4_f = flips(*edges[id4])
                for i_,e4_ in enumerate(edges_id4_f):
                    e4_next = edges_id4_f[(i_+1)%4]
                    if checkTwoSide(e_a3,e_b,e4_,e4_next):
                        res_4ed.append([visited+[id4],
                                           # edges[id4][(i_+3)%4],
                                           # last4e+[edges[id4][(i_+2)%4]],
                                           flip(edges[id4][(i_+3)%4]),
                                           last4e+[flip(edges[id4][(i_+2)%4])],
                                           ell,
                                       ])

        # for r4 in res_4ed:print('r4:',r4)
        print('len res4',len(res_4ed))

        # 找第5块：
        res_5ed = []
        for visited,e_b,last4e,ell in res_4ed:
            for id5 in range(1,6):
                if id5 in visited:continue
                for i_,e5_ in enumerate(edges[id5]):
                    e5_next = edges[id5][(i_+1)%4]
                    e5_next2 = edges[id5][(i_+2)%4]
                    if checkThreeSide(e_b,e_a4,ell,e5_,e5_next,e5_next2):
                        res_5ed.append([visited+[id5],last4e+[flip(edges[id5][(i_+3)%4])]])
                edges_id5_f = flips(*edges[id5])
                for i_,e5_ in enumerate(edges_id5_f):
                    e5_next = edges_id5_f[(i_+1)%4]
                    e5_next2 = edges_id5_f[(i_+2)%4]
                    # if checkThreeSide(ell,e_a4,e_b,e5_,e5_next,e5_next2):
                    if checkThreeSide(e_b,e_a4,ell,e5_,e5_next,e5_next2):
                        # res_5ed.append([visited+[id5],last4e+[edges_id5_f[(i_+3)%4]]])
                        res_5ed.append([visited+[id5],last4e+[flip(edges[id5][(i_+3)%4])]])

        # for r5 in res_5ed:print('r5:',r5)
        print('len res5',len(res_5ed))

        # 找第6块:
        res = []
        for visited,last4e in res_5ed:
            for id6 in range(1,6):
                if id6 in visited:continue
                # print(visited,last4e,id6)
                for i_,e6_ in enumerate(edges[id6]):
                    e6_next = edges[id6][(i_+1)%4]
                    e6_next2 = edges[id6][(i_+2)%4]
                    e6_next3 = edges[id6][(i_+3)%4]
                    if checkFourSide(*last4e,e6_,e6_next,e6_next2,e6_next3):
                        res.append(visited+[id6])
                        # return True

                edges_id6_f = flips(*edges[id6])
                for i_,e6_ in enumerate(edges_id6_f):
                    e6_next = edges_id6_f[(i_+1)%4]
                    e6_next2 = edges_id6_f[(i_+2)%4]
                    e6_next3 = edges_id6_f[(i_+3)%4]
                    if checkFourSide(*last4e,e6_,e6_next,e6_next2,e6_next3):
                        res.append(visited+[id6])
                        # return True

        for r6 in res:print(r6)
        print('len res',len(res))
        return False



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.composeCube(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        # [[["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]],
        # [[["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]],
        # [[["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["111","010","000"]]],
        [[["010","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","110"],["010","010","000"]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
