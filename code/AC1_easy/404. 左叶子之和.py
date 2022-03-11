# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 9:03
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 404. 左叶子之和.py
# @Software: PyCharm
# ===================================
"""给定二叉树的根节点 root ，返回所有左叶子之和。

 

示例 1：



输入: root = [3,9,20,null,null,15,7]
输出: 24
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
示例 2:

输入: root = [1]
输出: 0
 

提示:

节点数在 [1, 1000] 范围内
-1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0
        res = root.left.val if (root.left and not root.left and not root.right) else self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    data = [List2Tree(data_test[0])]  # list转node
    return s.sumOfLeftLeaves(*data)


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
        [[1,2,3,4,5]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
