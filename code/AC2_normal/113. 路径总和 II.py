# -*- coding: utf-8 -*-
# @Time    : 2021/11/19 16:11
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 113. 路径总和 II.py
# @Software: PyCharm
# ===================================
"""给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

 

示例 1：


输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
示例 2：


输入：root = [1,2,3], targetSum = 5
输出：[]
示例 3：

输入：root = [1,2], targetSum = 0
输出：[]
 

提示：

树中节点总数在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        测试case：
[]
0
[1,2]
1
        """
        self.res = []

    def dfs(self,root,route,remain):
        if root:
            route.append(root.val)
            if remain==root.val and not root.left and not root.right:
                self.res.append(route.copy())
            else:
                self.dfs(root.left,route.copy(),remain-root.val)
                self.dfs(root.right,route.copy(),remain-root.val)


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfs(root,[],targetSum)
        return self.res


    def hasPathSum_112_路径总和(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False
        targetSum -= root.val
        if root.left is None and root.right is None:return targetSum==0
        else: return self.hasPathSum_112_路径总和(root.left,targetSum) or self.hasPathSum_112_路径总和(root.right,targetSum)

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.pathSum(*data)


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
