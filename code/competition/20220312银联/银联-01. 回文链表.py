# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 16:59
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 银联-01. 回文链表.py
# @Software: PyCharm 
# ===================================
"""给定一个链表的头结点 head，判断链表删除一个节点后是否可以成为「回文链表」。
若可以，则返回 true；否则返回 false

注意：

输入用例均保证链表长度 大于等于 3
示例 1：

输入：head = [1,2,2,3,1]

输出：true

解释：如下图所示，蓝色结点为删除的结点
删除该节点后，链表为「回文链表」 [1,2,2,1]，返回 true
image.png

示例 2：

输入：head = [5,1,8,8,1,5]

输出：true

解释： 删除节点值为 8 的节点

示例 3：

输入：head = [1,2,3,4]

输出：false

提示：

链表中节点数目在范围 [3, 10^5]
0 <= Node.val <= 10
"""
from leetcode_python.utils import *

def Node2List(head:ListNode)->List:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

class Solution_wtl:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = Node2List(head)
        # nums = [str(x)for x in nums]
        return any(nums[:i]+nums[i+1:]==nums[-1:i:-1]+nums[i-1:-1:-1] for i in range(len(nums)))
        # for i in range(len(nums)):
        #     # s = nums[:i]+nums[i+1:]
        #     # if s==s[::-1]:return True
        #     if nums[:i]+nums[i+1:]==nums[-1:i:-1]+nums[i-1:-1:-1]:return True
        # return False


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        num = []
        while head != None:
            num.append(head.val)
            head = head.next

        def check(i, j):
            while i < j:
                if num[i] != num[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(num) - 1
        while i < j:
            if num[i] != num[j]:
                return check(i + 1, j) or check(i, j - 1)
            i += 1
            j -= 1
        return True

def test(data_test):
    s = Solution()
    data = data_test  # normal
    data = [List2Node(data_test[0])]  # list转node
    return s.isPalindrome(*data)


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
        [[1,2,4,5,6]],
        # [[5,5,10,10,5,5]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

