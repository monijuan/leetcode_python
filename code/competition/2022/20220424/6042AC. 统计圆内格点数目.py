# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6042AC. 统计圆内格点数目.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for x,y,r in circles:
            for x_ in range(x-r,x+r+1):
                for y_ in range(y-r,y+r+1):
                    if (x-x_)**2+(y-y_)**2<=r**2:
                        res.add((x_,y_))
        return len(res)


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countLatticePoints(*data)

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
        [[[2,2,2],[3,4,1]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
