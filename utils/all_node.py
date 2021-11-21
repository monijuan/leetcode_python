# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 23:28
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : all_node.py
# @Software: PyCharm 
# ===================================
class Node_116:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        """116. 填充每个节点的下一个右侧节点指针"""
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Node_430:
    def __init__(self, val, prev, next, child):
        """430. 扁平化多级双向链表"""
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Node_559:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{str(self.val)}->{self.next}"

    def reverse(self,head,tail):
        """反转指定头尾部分的链表"""
        now_next = tail.next
        now = head
        while now_next!=tail:
            now.next, now, now_next = now_next, now.next, now
        return tail,head

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        res = f'[{self.val}({self.left},{self.right})]'
        return res