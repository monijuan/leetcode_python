# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 20:45
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day06_32 - II. 从上到下打印二叉树 II.py
# @Software: PyCharm 
# ===================================
"""
"""
import time
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        pass

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        next_level = [root]
        while next_level:
            this_level = next_level
            next_level = []
            res_level = []
            while this_level:
                head = this_level.pop(0)
                if head:
                    res_level.append(head.val)
                    next_level.append(head.left)
                    next_level.append(head.right)
            if res_level:
                res.append(res_level)
        return res


def test(data_test):
    s = Solution()
    return s.getResult(*data_test)


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