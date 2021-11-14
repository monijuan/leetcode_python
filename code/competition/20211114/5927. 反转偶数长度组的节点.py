# -*- coding: utf-8 -*-
# @Time    : 2021/11/14 10:37
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5927. 反转偶数长度组的节点.py
# @Software: PyCharm 
# ===================================
"""给你一个链表的头节点 head 。

链表中的节点 按顺序 划分成若干 非空 组，这些非空组的长度构成一个自然数序列（1, 2, 3, 4, ...）。一个组的 长度 就是组中分配到的节点数目。换句话说：

节点 1 分配给第一组
节点 2 和 3 分配给第二组
节点 4、5 和 6 分配给第三组，以此类推
注意，最后一组的长度可能小于或者等于 1 + 倒数第二组的长度 。

反转 每个 偶数 长度组中的节点，并返回修改后链表的头节点 head 。



示例 1：



输入：head = [5,2,6,3,9,1,7,3,8,4]
输出：[5,6,2,3,9,1,4,8,3,7]
解释：
- 第一组长度为 1 ，奇数，没有发生反转。
- 第二组长度为 2 ，偶数，节点反转。
- 第三组长度为 3 ，奇数，没有发生反转。
- 最后一组长度为 4 ，偶数，节点反转。
示例 2：



输入：head = [1,1,0,6]
输出：[1,0,1,6]
解释：
- 第一组长度为 1 ，没有发生反转。
- 第二组长度为 2 ，节点反转。
- 最后一组长度为 1 ，没有发生反转。
示例 3：



输入：head = [2,1]
输出：[2,1]
解释：
- 第一组长度为 1 ，没有发生反转。
- 最后一组长度为 1 ，没有发生反转。
示例 4：

输入：head = [8]
输出：[8]
解释：只有一个长度为 1 的组，没有发生反转。


提示：

链表中节点数目范围是 [1, 105]
0 <= Node.val <= 105
"""
from leetcode_python.utils import *


class Solution:

    def reverseList_num(self, head: ListNode, times:int):
        if head is None:return head
        start = head
        new_head,last = None,None
        while start and times:
            next = start.next
            start.next = new_head
            new_head = start
            if last is None:last = new_head
            start = next
            times-=1
        last.next = start
        return new_head

    def reverseEvenLengthGroups_not_judge_last(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        new_head = ListNode(None,next=head)
        while new_head:
            if length&1==0:
                now_head = new_head
                res_head = self.reverseList_num(new_head.next,length)
                new_head = now_head
                new_head.next = res_head
            move_time = length
            while new_head and move_time:
                new_head = new_head.next
                move_time-=1
            length+=1
        return head


    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass





def test(data_test):
    s = Solution()
    return s.reverseEvenLengthGroups(*data_test)


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