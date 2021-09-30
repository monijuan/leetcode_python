# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 15:15
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 102. 二叉树的层序遍历.py
# @Software: PyCharm
# ===================================
"""给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        this_line = [root]
        while this_line:
            res_line = []
            next_line = []
            for node in this_line:
                res_line.append(node.val)
                if node.left:next_line.append(node.left)
                if node.right:next_line.append(node.right)
            res.append(res_line)
            this_line = next_line
        return res


def test(data_test):
    s = Solution()
    return s.levelOrder(*data_test)


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
