# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 23:28
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : all_node.py
# @Software: PyCharm 
# ===================================


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        # return str(self.val)
        res = f'[{self.val},l:{self.left},r:{self.right}]'
        return res