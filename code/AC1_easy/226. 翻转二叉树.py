# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 17:12
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 226. 翻转二叉树.py
# @Software: PyCharm
# ===================================
"""翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    class Solution:
        def invertTree(self, root: TreeNode) -> TreeNode:
            if root:
                new = TreeNode()
                new.val = root.val
                new.left = self.invertTree(root.right)
                new.right = self.invertTree(root.left)
                return new
            else:
                return None


def test(data_test):
    s = Solution()
    return s.getResult(*data_test)


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
