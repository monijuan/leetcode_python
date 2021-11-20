# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 7:49
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 415. 字符串相加.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def addStrings(self, num1: str, num2: str) -> str:
        # 把每一位的求和保留到对应指数位的数组里
        len1,len2 = len(num1),len(num2)
        saves = [[] for _ in range(max(len1,len2)+1)]
        num1_int_r = [int(x) for x in num1[::-1]]
        num2_int_r = [int(x) for x in num2[::-1]]
        for pow in range(max(len1,len2)):
            if pow<len1 and pow<len2:
                saves[pow].append(num1_int_r[pow]+num2_int_r[pow])
            elif pow<len1:
                saves[pow].append(num1_int_r[pow])
            else:
                saves[pow].append(num2_int_r[pow])

        # 每一位数组求和，十位以上部分进位
        res_r = []
        pow=0
        while pow<len(saves):
            sum_now = sum(saves[pow])
            res_r.append(sum_now%10)
            remain = sum_now//10
            if remain:
                if pow<len(saves):
                    saves[pow+1].append(remain)
                else:
                    saves.append([remain])
            pow+=1

        # 去除结尾多余的0，逆序拼接字符串
        while len(res_r)>1 and res_r[-1]==0: res_r.pop(-1)
        return ''.join([str(x)for x in res_r[::-1]])

    def multiply_043_字符串相乘(self, num1: str, num2: str) -> str:
        # 把每一位的乘积保留到对应指数位的数组里
        saves = [[] for _ in range(len(num1)+len(num2))]
        num1_int_r = [int(x) for x in num1[::-1]]
        num2_int_r = [int(x) for x in num2[::-1]]
        for pow1,n1 in enumerate(num1_int_r):
            for pow2,n2 in enumerate(num2_int_r):
                saves[pow1+pow2].append(n1*n2)

        # 每一位数组求和，十位以上部分进位
        res_r = []
        pow=0
        while pow<len(saves):
            sum_now = sum(saves[pow])
            res_r.append(sum_now%10)
            remain = sum_now//10
            if remain:
                if pow<len(saves):
                    saves[pow+1].append(remain)
                else:
                    saves.append([remain])
            pow+=1

        # 去除结尾多余的0，逆序拼接字符串
        while len(res_r)>1 and res_r[-1]==0: res_r.pop(-1)
        return ''.join([str(x)for x in res_r[::-1]])

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.addStrings(*data)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')