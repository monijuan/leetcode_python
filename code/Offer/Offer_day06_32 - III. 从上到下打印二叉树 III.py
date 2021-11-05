# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 21:16
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day06_32 - III. 从上到下打印二叉树 III.py
# @Software: PyCharm 
# ===================================
"""请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        pass

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        next_level = [root]
        while next_level:
            this_level = next_level
            next_level = []
            res_level = []
            while this_level:
                head = this_level.pop(0)
                if head:
                    res_level.append(head.val)
                    next_level.append(head.left)
                    next_level.append(head.right)
            if res_level :
                if len(res)&1:
                    res.append(res_level[::-1])
                else:
                    res.append(res_level)
        return res


def test(data_test):
    s = Solution()
    return s.levelOrder(*data_test)


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