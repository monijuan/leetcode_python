# -*- coding: utf-8 -*-
# @Time    : 2021/11/20 19:42
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 103. 二叉树的锯齿形层序遍历.py
# @Software: PyCharm 
# ===================================
"""
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        this_line = [root]
        reverse = False
        while this_line:
            res_line = []
            next_line = []
            for node in this_line:
                res_line.append(node.val)
                if node.left:next_line.append(node.left)
                if node.right:next_line.append(node.right)
            if reverse:
                res.append(res_line[::-1])
            else:
                res.append(res_line)
            reverse = not reverse
            this_line = next_line
        return res

    def levelOrder_102_二叉树的层序遍历(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        this_line = [root]
        while this_line:
            res_line = []
            next_line = []
            for node in this_line:
                res_line.append(node.val)
                if node.left:next_line.append(node.left)
                if node.right:next_line.append(node.right)
            res.append(res_line)
            this_line = next_line
        return res

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.multiply(*data)


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