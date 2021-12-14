# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 9:13
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 572. 另一棵树的子树.py
# @Software: PyCharm
# ===================================
"""给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。

二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。

 

示例 1：


输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
示例 2：


输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
 

提示：

root 树上的节点数量范围是 [1, 2000]
subRoot 树上的节点数量范围是 [1, 1000]
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        错误case：
            [3,4,5,1,null,2],[3,1,2]
            [3,4,5,1,2],[4,1,2,1]
            [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2],[1,null,1,null,1,null,1,null,1,null,1,2]
        """
        pass

    @lru_cache(None)
    def isSame(self,r1,r2):
        if not r1 and not r2:return True
        elif not r1 or not r2:return False
        elif r1.val==r2.val and self.isSame(r1.left,r2.left) and self.isSame(r1.right,r2.right):return True
        else:return False

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot and not root:return True
        elif not subRoot or not root:return False
        elif self.isSame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot):return True
        else:return False


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.isSubtree(*data)


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
