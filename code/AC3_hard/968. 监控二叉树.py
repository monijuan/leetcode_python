# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 15:31
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 968. 监控二叉树.py
# @Software: PyCharm
# ===================================
"""给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

 

示例 1：



输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
示例 2：



输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-cameras
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        参考大佬：https://leetcode-cn.com/problems/binary-tree-cameras/solution/dfs-hou-xu-bian-li-tan-xin-chao-jian-ji-1t0r1/
        """
        self.res = 0

    def dfs(self,now, father):
        if now:
            self.dfs(now.left, now)
            self.dfs(now.right, now)
            if (now.left and now.left.val!=1) or (now.right and now.right.val!=1):
                now.val = 1
                father.val = 1
                self.res += 1

    def minCameraCover(self, root: TreeNode) -> int:
        self.dfs(root,root)
        return self.res+1 if root.val == 0 else self.res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.minCameraCover(*data)


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
