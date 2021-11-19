# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 17:24
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 199. 二叉树的右视图.py
# @Software: PyCharm
# ===================================
"""给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

示例 1:



输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
示例 2:

输入: [1,null,3]
输出: [1,3]
示例 3:

输入: []
输出: []
 

提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def rightSideView(self, root: TreeNode) -> List[int]:
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
            res.append(res_line[-1])
            this_line = next_line
        return res


    def levelOrder_102_二叉树的层序遍历(self, root: TreeNode) -> List[List[int]]:
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
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.rightSideView(*data)


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
