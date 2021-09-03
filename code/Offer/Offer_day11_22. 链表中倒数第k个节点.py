# -*- coding: utf-8 -*-
# @Time    : 2021/9/2 7:14
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day11_22. 链表中倒数第k个节点.py
# @Software: PyCharm 
# ===================================
"""输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        pass

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        res = head
        diff = 0
        while diff<k:
            diff+=1
            head = head.next
        while head:
            res = res.next
            head=head.next
        return res


def test(data_test):
    """
    data_test = [[1, 2, 3, 4, 5], 2]
    """
    s = Solution()
    nextnode = None
    for x in data_test[0][::-1]:
        head = ListNode(x)
        head.next = nextnode
        nextnode = head
    return s.getKthFromEnd(head,data_test[1])


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
        [[1,2,3,4,5], 2],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')