# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 20:00
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 061. 旋转链表.py
# @Software: PyCharm
# ===================================
"""给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]
 

提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

k=1
nums = [1,3,4,5]
print(nums[-k:],nums[:-k])
nums = nums[-k:]+nums[:k+1]
print(nums)

def List2Node(datas:List)->ListNode:
    """列表 -> 链表"""
    hair = ListNode(None)
    head = hair
    for data in datas:
         head.next = ListNode(data)
         head = head.next
    return hair.next
def Node2List(head:ListNode)->List:
    """链表 -> 列表"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:return head
        nums = Node2List(head)
        if len(nums)==1:return head
        k %= len(nums)
        nums = nums[-k:]+nums[:-k]
        return List2Node(nums)


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
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
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
