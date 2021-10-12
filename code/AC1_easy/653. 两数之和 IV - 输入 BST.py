# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 9:05
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 653. 两数之和 IV - 输入 BST.py
# @Software: PyCharm
# ===================================
"""给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

 

示例 1：


输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
示例 2：


输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
示例 3：

输入: root = [2,1,3], k = 4
输出: true
示例 4：

输入: root = [2,1,3], k = 1
输出: false
示例 5：

输入: root = [2,1,3], k = 3
输出: true
 

提示:

二叉树的节点个数的范围是  [1, 104].
-104 <= Node.val <= 104
root 为二叉搜索树
-105 <= k <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findTarget(self, root: TreeNode, k: int) -> bool:
        inorder_list = []
        self.inorder(root,inorder_list)
        print(inorder_list)

        left,right = 0,len(inorder_list)-1
        while left<right:
            sum = inorder_list[left]+inorder_list[right]
            if sum==k:return True
            elif sum>k:right-=1
            else:left+=1
        return False

    def inorder(self, root: TreeNode, inorder_list)->None:
        if root:
            self.inorder(root.left,inorder_list)
            inorder_list.append(root.val)
            self.inorder(root.right,inorder_list)

def test(data_test):
    s = Solution()
    return s.findTarget(*data_test)


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
