# -*- coding: utf-8 -*-
# @Time    : 2021/9/28 13:16
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 437. 路径总和 III.py
# @Software: PyCharm
# ===================================
"""给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def dfs(self, root: TreeNode, targetSum: int, sum_now: int) -> int:
        if not root: return 0
        res = 0
        sum_now += root.val
        if sum_now==targetSum:res+=1
        res += self.dfs(root.left,targetSum,sum_now)
        res += self.dfs(root.right,targetSum,sum_now)
        return res

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root: return 0
        res = self.dfs(root, targetSum, 0)
        res += self.pathSum(root.left,targetSum)
        res += self.pathSum(root.right,targetSum)
        return res


def test(data_test):
    s = Solution()
    return s.pathSum(*data_test)


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
