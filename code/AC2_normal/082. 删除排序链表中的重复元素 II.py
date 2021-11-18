# -*- coding: utf-8 -*-
# @Time    : 2021/11/18 15:19
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 082. 删除排序链表中的重复元素 II.py
# @Software: PyCharm
# ===================================
"""存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。

返回同样按升序排列的结果链表。

 

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        hair = ListNode(None,head)
        last,now = hair,hair.next
        while now:
            if now.next and now.val==now.next.val:
                while now.next and now.val==now.next.val:
                    now = now.next
                now = now.next  # now是重复的，保留next
                last.next = now # 无论是否有重复，上一个的下一个都会发生改变
            else:
                last.next = now # 无论是否有重复，上一个的下一个都会发生改变
                last,now = last.next,now.next    # 只有当没有重复的时候，才会后移
        return hair.next


def test(data_test):
    s = Solution()
    # data = data_test  # normal
    data = [list2node(data_test[0])]  # list转node
    return s.deleteDuplicates(*data)


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
        [[1,2,3,3,4,4,5]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
