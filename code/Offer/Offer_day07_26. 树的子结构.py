# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 22:34
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day07_26. 树的子结构.py
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

    def isSame(self, A: TreeNode, B: TreeNode) -> bool:
        if A is not None and B is not None:
            if B.val==A.val:
                return self.isSame(A.left,B.left) and self.isSame(A.right,B.right)
            else:
                return False
        elif B is None:
            return True
        else:
            return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:return False
        queue = [A]
        while len(queue):
            head = queue.pop(0)
            if head:
                if self.isSame(head,B):return True
                queue.append(head.left)
                queue.append(head.right)
        return False

class Solution_官方:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


def test(data_test):
    s = Solution()
    return s.isSubStructure(*data_test)


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