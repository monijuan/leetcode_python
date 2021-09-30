# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 15:13
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 145. 二叉树的后序遍历.py
# @Software: PyCharm
# ===================================
"""给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root: TreeNode)->None:
        if root:
            self.res.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.preorder(root)
        return self.res

    def inorder(self, root: TreeNode)->None:
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inorder(root)
        return self.res

    def postorder(self, root: TreeNode)->None:
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.res.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.postorder(root)
        return self.res


def test(data_test):
    s = Solution()
    return s.postorderTraversal(*data_test)


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
