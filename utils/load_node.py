# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 14:57
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : load_node.py
# @Software: PyCharm
# ===================================
from typing import List,Callable,Optional
from .all_node import *

def list2node(datas:List)->ListNode:
    hair = ListNode(None)
    head = hair
    for data in datas:
         head.next = ListNode(data)
         head = head.next
    return hair.next

if __name__ == '__main__':
    node = list2node([1,2,3,4])
    print(node)

