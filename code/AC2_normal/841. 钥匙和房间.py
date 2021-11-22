# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 9:26
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 841. 钥匙和房间.py
# @Software: PyCharm
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """有回路的层序遍历"""
        pass

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        notvis = set(range(1,len(rooms)))
        remain = [0]
        while remain:
            next = remain.pop(-1)
            for key in rooms[next]:
                if key in notvis:
                    remain.append(key)
                    notvis.remove(key)
        return len(notvis)==0


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.canVisitAllRooms(*data)


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
        [[[1],[2],[3],[]]],
        [[[1,3],[3,0,1],[2],[0]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
