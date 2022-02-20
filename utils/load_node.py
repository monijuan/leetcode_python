# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 14:57
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : load_node.py
# @Software: PyCharm
# ===================================
from typing import List,Callable,Optional
from .all_node import *

# region ############ list 2 others
def List2Tree(data):
    """列表（or字符串） -> 二叉树"""
    if isinstance(data, str): data = eval(data)
    length = len(data)
    if 0 == length: return None
    head = TreeNode(data[0])
    queue = [head]
    index = 1
    while index < length:
        node = queue.pop(0)
        data_index = data[index]
        if data_index is not None:
            node.left = TreeNode(int(data_index))
            queue.append(node.left)
        index += 1
        if index >= length: break
        data_index = data[index]
        if data_index is not None:
            node.right = TreeNode(int(data_index))
            queue.append(node.right)
        index += 1
    return head

def List2BST(nums: List[int]) -> TreeNode:
    """列表 -> 平衡二叉树"""
    length = len(nums)
    if length == 1:
        return TreeNode(nums[0])
    elif length == 2:
        return TreeNode(nums[0], right=TreeNode(nums[1]))
    else:
        root = TreeNode(nums[length // 2])
        root.left = List2BST(nums[:length // 2])
        root.right = List2BST(nums[length // 2 + 1:])
        return root

def List2Node(datas:List)->ListNode:
    """列表 -> 链表"""
    hair = ListNode(None)
    head = hair
    for data in datas:
         head.next = ListNode(data)
         head = head.next
    return hair.next

# endregion

# region ############ others 2 list
def Node2List(head:ListNode)->List:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def BST2List(root):
    """平衡二叉树 -> 列表"""
    return BST2List(root.left) + [root.val] + BST2List(root.right) if root else []

def Tree2List(root):
    """二叉树 -> 列表"""
    if not root:return []
    res = []
    last = [root]
    while last:
        now = []
        for node in last:
            if node:
                res.append(node.val)
                now.append(node.left)
                now.append(node.right)
            else:
                res.append(None)
        last = now
    while len(res)>1 and res[-1]==None: res.pop(-1)
    return res

# endregion


if __name__ == '__main__':
    node = List2Node([1,2,3,4])
    print(node)

