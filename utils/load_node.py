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

def list2BST(nums: List[int]) -> TreeNode:
    length = len(nums)
    if length == 1:
        return TreeNode(nums[0])
    elif length == 2:
        return TreeNode(nums[0], right=TreeNode(nums[1]))
    else:
        root = TreeNode(nums[length // 2])
        root.left = list2BST(nums[:length // 2])
        root.right = list2BST(nums[length // 2 + 1:])
        return root

def list2node(datas:List)->ListNode:
    hair = ListNode(None)
    head = hair
    for data in datas:
         head.next = ListNode(data)
         head = head.next
    return hair.next

# endregion

# region ############ others 2 list
def BST2list(root):
    """
        if root.left and root.right:
            return BST2list(root.left) + [root.val] + BST2list(root.right)
        elif root.left:
            return BST2list(root.left) + [root.val]
        elif root.right:
            return [root.val] + BST2list(root.right)
        else:
            return [root.val]
    """
    return BST2list(root.left) + [root.val] + BST2list(root.right) if root else []

# endregion


if __name__ == '__main__':
    node = list2node([1,2,3,4])
    print(node)

