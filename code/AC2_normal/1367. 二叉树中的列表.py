# -*- coding: utf-8 -*-
# @Time    : 2022/3/19 9:45
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1367. 二叉树中的列表.py
# @Software: PyCharm 
# ===================================
"""给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。

如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。

一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

 

示例 1：



输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。
示例 2：



输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
示例 3：

输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在一一对应链表的路径。
 

提示：

二叉树和链表中的每个节点的值都满足 1 <= node.val <= 100 。
链表包含的节点数目在 1 到 100 之间。
二叉树包含的节点数目在 1 到 2500 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

def check(head,root):
    if not head:return True
    if not root:return False
    if root.val==head.val:
        return check(head.next,root.left) or check(head.next,root.right)
    else:
        return False

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if root and check(head,root):return True
        if root.left and self.isSubPath(head,root.left):return True
        if root.right and self.isSubPath(head,root.right):return True
        return False


def test(data_test):
    s = Solution()
    data = data_test  # normal
    data = [List2Node(data_test[0]),List2Tree(data_test[1])]  # list转node
    return s.isSubPath(*data)


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
        [[4,2,8],[1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

