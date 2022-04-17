# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 22:08
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 52. 二叉搜索树染色.py
# @Software: PyCharm 
# ===================================
"""欢迎各位勇者来到力扣城，本次试炼主题为「二叉搜索树染色」。

每位勇士面前设有一个二叉搜索树的模型，模型的根节点为 root，树上的各个节点值均不重复。初始时，所有节点均为蓝色。现在按顺序对这棵二叉树进行若干次操作， ops[i] = [type, x, y] 表示第 i 次操作为：

type 等于 0 时，将节点值范围在 [x, y] 的节点均染蓝
type 等于 1 时，将节点值范围在 [x, y] 的节点均染红
请返回完成所有染色后，该二叉树中红色节点的数量。

注意：

题目保证对于每个操作的 x、y 值定出现在二叉搜索树节点中
示例 1：

输入：root = [1,null,2,null,3,null,4,null,5], ops = [[1,2,4],[1,1,3],[0,3,5]]

输出：2

解释：
第 0 次操作，将值为 2、3、4 的节点染红；
第 1 次操作，将值为 1、2、3 的节点染红；
第 2 次操作，将值为 3、4、5 的节点染蓝；
因此，最终值为 1、2 的节点为红色节点，返回数量 2
image.png

示例 2：

输入：root = [4,2,7,1,null,5,null,null,null,null,6]
ops = [[0,2,2],[1,1,5],[0,4,5],[1,5,7]]

输出：5

解释：
第 0 次操作，将值为 2 的节点染蓝；
第 1 次操作，将值为 1、2、4、5 的节点染红；
第 2 次操作，将值为 4、5 的节点染蓝；
第 3 次操作，将值为 5、6、7 的节点染红；
因此，最终值为 1、2、5、6、7 的节点为红色节点，返回数量 5
image.png

提示：

1 <= 二叉树节点数量 <= 10^5
1 <= ops.length <= 10^5
ops[i].length == 3
ops[i][0] 仅为 0 or 1
0 <= ops[i][1] <= ops[i][2] <= 10^9
0 <= 节点值 <= 10^9
"""
from leetcode_python.utils import *

from sortedcontainers import SortedList

class tree_线段树():
    def __init__(self, N, query_fn=sum):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = val
        if x < self.N:
            self.lazy[x] = val

    def _pull(self, x):
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])
            # self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])
            self.tree[x] = self.lazy[x]

    def _push(self, x):
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, val):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, val)
                L += 1
            if R & 1 == 0:
                self._apply(R, val)
                R -= 1
            L //= 2
            R //= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):
        L += self.N
        R += self.N
        self._push(L)
        self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return ans



class Solution:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        nums = BST2List(root)
        nums = [x for x in nums if x != None]
        print(nums)
        tree = tree_线段树(max(nums)+1,query_fn=max)
        for t,x,y in ops:
            tree.update(x,y,t)
            print(tree.lazy)


# --------------------------------------------------------------------------------

def BST2List(root):
    return BST2List(root.left) + [root.val] + BST2List(root.right) if root else []

class Solution_1:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        nums = BST2List(root)
        nums = [x for x in nums if x != None]
        n = len(nums)
        d1 = defaultdict(list)
        d2 = defaultdict(list)
        for i, (t, x, y) in enumerate(ops):
            p = bisect.bisect_left(nums, x)
            if p < n: d1[p].append([i, t])
            p = bisect.bisect_right(nums, y)
            if p < n: d2[p].append([i, t])
        ans = 0
        sl = SortedList()
        for i in range(n):
            for tp in d1[i]: sl.add(tp)
            for tp in d2[i]: sl.remove(tp)
            if sl and sl[-1][1] == 1: ans += 1
        return ans

# --------------------------------------------------------------------------------

def BST2List(root):
    return BST2List(root.left) + [root.val] + BST2List(root.right) if root else []

class Solution_2:
    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        nums = BST2List(root)
        ans = 0
        for op in ops[::-1]:
            l = bisect.bisect_left(nums,op[1])
            r = bisect.bisect(nums,op[2]) - 1
            if l > r: continue
            if op[0]==1:   ans += r - l + 1
            nums[l:r+1] = []
        return ans

def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getNumber(List2BST(data[0]),*data[1:])

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
        [[1,None,2,None,3,None,4,None,5],[[1,2,4],[1,1,3],[0,3,5]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
