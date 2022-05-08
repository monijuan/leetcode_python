# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 10:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6057AC. 统计值等于子树平均值的节点数.py
# @Software: PyCharm 
# ===================================
"""给你一棵二叉树的根节点 root ，找出并返回满足要求的节点数，要求节点的值等于其 子树 中值的 平均值 。

注意：

n 个元素的平均值可以由 n 个元素 求和 然后再除以 n ，并 向下舍入 到最近的整数。
root 的 子树 由 root 和它的所有后代组成。


示例 1：


输入：root = [4,8,5,0,1,null,6]
输出：5
解释：
对值为 4 的节点：子树的平均值 (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4 。
对值为 5 的节点：子树的平均值 (5 + 6) / 2 = 11 / 2 = 5 。
对值为 0 的节点：子树的平均值 0 / 1 = 0 。
对值为 1 的节点：子树的平均值 1 / 1 = 1 。
对值为 6 的节点：子树的平均值 6 / 1 = 6 。
示例 2：


输入：root = [1]
输出：1
解释：对值为 1 的节点：子树的平均值 1 / 1 = 1。


提示：

树中节点数目在范围 [1, 1000] 内
0 <= Node.val <= 1000
"""
from leetcode_python.utils import *


def dfs(root: Optional[TreeNode]):
    if root.left and root.right:
        suml,cntl,resl = dfs(root.left)
        sumr,cntr,resr = dfs(root.right)
        res_cnt = cntl+cntr+1
        res_sum = root.val+suml+sumr
        ave = res_sum//res_cnt
        res = resl+resr+int(ave==root.val)
        print(root.val,res_sum,res_cnt,res)
        return res_sum,res_cnt,res
    elif root.left:
        suml, cntl, resl = dfs(root.left)
        res_cnt = cntl+1
        res_sum = root.val+suml
        ave = res_sum//res_cnt
        res = resl+int(ave==root.val)
        return res_sum,res_cnt,res
    elif root.right:
        suml, cntl, resl = dfs(root.right)
        res_cnt = cntl+1
        res_sum = root.val+suml
        ave = res_sum//res_cnt
        res = resl+int(ave==root.val)
        return res_sum,res_cnt,res
    else:
        return root.val,1,1

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        sum,cnt,res = dfs(root)
        return res


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
