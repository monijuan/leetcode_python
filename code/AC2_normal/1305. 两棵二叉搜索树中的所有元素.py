# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 0:16
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1305. 两棵二叉搜索树中的所有元素.py
# @Software: PyCharm 
# ===================================
"""给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 

提示：

每棵树的节点数在 [0, 5000] 范围内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


def Tree2List(root):
    """二叉树 -> 列表"""
    if not root:return []
    res = []
    last = [root]
    while last:
        now = []
        for node in last:
            if node:
                res.append(node.val)
                now.append(node.left)
                now.append(node.right)
            else:
                res.append(None)
        last = now
    while len(res)>1 and res[-1]==None: res.pop(-1)
    return res

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums1 = [x for x in Tree2List(root1) if x!=None]
        nums2 = [x for x in Tree2List(root2) if x!=None]
        return list(sorted(nums1 + nums2))


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
