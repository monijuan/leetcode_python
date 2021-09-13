# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 16:24
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 105. 从前序与中序遍历序列构造二叉树.py
# @Software: PyCharm
# ===================================
"""输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

示例 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
示例 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==1: return TreeNode(preorder[0])
        for id,num in enumerate(inorder):
            if num==preorder[0]:
                head = TreeNode(num)
                head.left=self.buildTree(preorder[1:id+1],inorder[:id])
                head.right=self.buildTree(preorder[id+1:],inorder[id+1:])
                return head


    def buildTree_copy(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==1: return TreeNode(preorder[0])
        preorder_ = [x for x in preorder]
        inorder_ = [x for x in inorder]
        for id,num in enumerate(inorder_):
            if num==preorder_[0]:
                head = TreeNode(num)
                # print(num,preorder,inorder)
                # print('left:',preorder[1:id+1],inorder[:id])
                # print('right:',preorder[id+1:],inorder[id+1:])
                head.left=self.buildTree(preorder_[1:id+1],inorder_[:id])
                head.right=self.buildTree(preorder_[id+1:],inorder_[id+1:])
                return head


def test(data_test):
    s = Solution()
    return s.buildTree(*data_test)


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
        [[3,9,20,15,7],[9,3,15,20,7]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
