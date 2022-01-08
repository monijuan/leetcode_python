# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 22:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 03.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def longestPalindrome(self, words: List[str]) -> int:
        pairset = defaultdict(int)
        sameset = defaultdict(int)
        pairs = 0
        ps = []
        for w in words:
            ws = w[::-1]
            if w==ws:sameset[w]+=1  # aa
            else:   # ab
                if pairset[ws]>0:
                    pairset[ws]-=1
                    pairs+=1
                    ps.append((w,ws))
                else:
                    pairset[w]+=1
        res = 4*pairs
        od =  False
        print(ps)
        print(pairset)
        print(sameset)
        print(pairs)
        for numsame in sameset.values():
            if numsame>0:
                if numsame&1:
                    od=True
                    numsame-=1
                res += 2*numsame
        if od:res+=2
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.longestPalindrome(*data)


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
        # [["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]],# 14
        [["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')