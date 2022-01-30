# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 10:00
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5944AC. 从二叉树一个节点到另一个节点每一步的方向.py
# @Software: PyCharm 
# ===================================
"""给你一棵 二叉树 的根节点 root ，这棵二叉树总共有 n 个节点。每个节点的值为 1 到 n 中的一个整数，且互不相同。给你一个整数 startValue ，表示起点节点 s 的值，和另一个不同的整数 destValue ，表示终点节点 t 的值。

请找到从节点 s 到节点 t 的 最短路径 ，并以字符串的形式返回每一步的方向。每一步用 大写 字母 'L' ，'R' 和 'U' 分别表示一种方向：

'L' 表示从一个节点前往它的 左孩子 节点。
'R' 表示从一个节点前往它的 右孩子 节点。
'U' 表示从一个节点前往它的 父 节点。
请你返回从 s 到 t 最短路径 每一步的方向。



示例 1：



输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
输出："UURL"
解释：最短路径为：3 → 1 → 5 → 2 → 6 。
示例 2：



输入：root = [2,1], startValue = 2, destValue = 1
输出："L"
解释：最短路径为：2 → 1 。


提示：

树中节点数目为 n 。
2 <= n <= 105
1 <= Node.val <= n
树中所有节点的值 互不相同 。
1 <= startValue, destValue <= n
startValue != destValue
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findRoute(self, root: TreeNode, p: int):
        if not root:return False,''
        elif root.val == p:
            return True,''
        else:
            isleft,rl = self.findRoute(root.left, p)
            isright,rr = self.findRoute(root.right, p)
            if isleft:
                return True,'L'+rl
            elif isright:
                return True,'R'+rr
            else:
                return False,''

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        _,routea = self.findRoute(root,startValue)
        _,routeb = self.findRoute(root,destValue)

        first = 0
        len1,len2 = len(routea),len(routeb)
        while first<min(len1,len2) and routea[first]==routeb[first]:first+=1
        res = "U"*(len1-first)+routeb[first::]
        return res



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getDirections(*data)


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
        [List2Tree([5,1,2,3,None,6,4]),3,6],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')