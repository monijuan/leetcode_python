# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 22:05
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 线段树.py
# @Software: PyCharm 
# ===================================

class tree_线段树():
    def __init__(self, N, update_fn=sum, query_fn=sum):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def _pull(self, x):
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x * 2], self.tree[x * 2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

    def _push(self, x):
        for h in range(self.H, 0, -1):
            y = x >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2 + 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                self._apply(R, h)
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


class tree_线段树_结点:
    def __init__(self, l: int, r: int):
        self.treesum = 0
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.add = 0
        self.mul = 1

    @property
    def _mid(self):
        return (self.l + self.r) // 2

    @property
    def _left(self):
        if self.left == None:
            self.left = tree_线段树_结点(self.l, self._mid)
        return self.left

    @property
    def _right(self):
        if self.right == None:
            self.right = tree_线段树_结点(self._mid + 1, self.r)
        return self.right

    def push_up(self) -> None:
        self.treesum = self._left.treesum + self._right.treesum
        self.treesum %= (10 ** 9 + 7)

    def add_update(self, ul: int, ur: int, addval: int) -> None:
        if ul <= self.l and self.r <= ur:
            self.treesum += (self.r - self.l + 1) * addval
            self.add += addval
            self.treesum %= (10 ** 9 + 7)
            return

        self.lazy_push_down()

        if ul <= self._mid:
            self._left.add_update(ul, ur, addval)
        if self._mid + 1 <= ur:
            self._right.add_update(ul, ur, addval)

        self.push_up()

    def mul_update(self, ul: int, ur: int, mulval: int) -> None:
        if ul <= self.l and self.r <= ur:
            self.treesum *= mulval
            self.add *= mulval
            self.mul *= mulval
            self.treesum %= (10 ** 9 + 7)
            self.add %= (10 ** 9 + 7)
            self.mul %= (10 ** 9 + 7)
            return

        self.lazy_push_down()

        if ul <= self._mid:
            self._left.mul_update(ul, ur, mulval)
        if self._mid + 1 <= ur:
            self._right.mul_update(ul, ur, mulval)

        self.push_up()

    def query(self, ql: int, qr: int) -> int:
        if qr < self.l or self.r < ql:
            return 0
        if ql <= self.l and self.r <= qr:
            return self.treesum

        self.lazy_push_down()

        range_sum = self._left.query(ql, qr) + self._right.query(ql, qr)
        return range_sum % (10 ** 9 + 7)

    def lazy_push_down(self) -> None:
        if self.add != 0 or self.mul != 1:
            # ---- 更新左子和右子的懒数据
            self._left.treesum = self._left.treesum * self.mul + (self._left.r - self._left.l + 1) * self.add
            self._right.treesum = self._right.treesum * self.mul + (self._right.r - self._right.l + 1) * self.add
            self._left.mul *= self.mul
            self._right.mul *= self.mul
            self._left.add = self._left.add * self.mul + self.add
            self._right.add = self._right.add * self.mul + self.add

            self._left.treesum %= (10 ** 9 + 7)
            self._right.treesum %= (10 ** 9 + 7)
            self._left.mul %= (10 ** 9 + 7)
            self._right.mul %= (10 ** 9 + 7)
            self._left.add %= (10 ** 9 + 7)
            self._right.add %= (10 ** 9 + 7)

            self.add = 0
            self.mul = 1



class Fancy_1622_奇妙序列_结点:

    def __init__(self):
        self.n = -1  # 实指
        self.ST = tree_线段树_结点(0, 10 ** 5)

    def append(self, val: int) -> None:
        self.n += 1
        self.ST.add_update(self.n, self.n, val)

    def addAll(self, inc: int) -> None:
        if self.n >= 0:  # 有个奇葩测试数据，上来就加
            self.ST.add_update(0, self.n, inc)

    def multAll(self, m: int) -> None:
        if self.n >= 0:
            self.ST.mul_update(0, self.n, m)

    def getIndex(self, idx: int) -> int:
        if self.n < idx:
            return -1
        return self.ST.query(idx, idx)


class tree_线段树_数组:
    def __init__(self, n: int):
        self.treesum = [0 for _ in range(4 * n)]
        self.n = n
        self.add = [0 for _ in range(4 * n)]
        self.mul = [1 for _ in range(4 * n)]

    def add_update(self, ul: int, ur: int, addval: int) -> None:
        self._add_update(0, 0, self.n - 1, ul, ur, addval)

    def mul_update(self, ul: int, ur: int, mulval: int) -> None:
        self._mul_update(0, 0, self.n - 1, ul, ur, mulval)

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n - 1, ql, qr)

    def push_up(self, root: int, l: int, r: int) -> None:
        left = 2 * root + 1
        right = 2 * root + 2
        self.treesum[root] = self.treesum[left] + self.treesum[right]
        self.treesum[root] %= (10 ** 9 + 7)

    def lazy_push_down(self, root: int, l: int, r: int) -> None:
        if self.add[root] != 0 or self.mul[root] != 1:
            left = 2 * root + 1
            right = 2 * root + 2
            self.treesum[left] = self.treesum[left] * self.mul[root] + self.add[root]
            self.treesum[right] = self.treesum[right] * self.mul[root] + self.add[root]
            self.mul[left] *= self.mul[root]
            self.mul[right] *= self.mul[root]
            self.add[left] = self.add[left] * self.mul[root] + self.add[root]
            self.add[right] = self.add[right] * self.mul[root] + self.add[root]

            self.treesum[left] %= (10 ** 9 + 7)
            self.treesum[right] %= (10 ** 9 + 7)
            self.mul[left] %= (10 ** 9 + 7)
            self.mul[right] %= (10 ** 9 + 7)
            self.add[left] %= (10 ** 9 + 7)
            self.add[right] %= (10 ** 9 + 7)

            self.mul[root] = 1
            self.add[root] = 0

    def _add_update(self, root: int, l: int, r: int, ul: int, ur: int, addval: int) -> None:
        if ul <= l and r <= ur:
            self.treesum[root] += (r - l + 1) * addval
            self.add[root] += addval
            self.treesum[root] %= (10 ** 9 + 7)
            self.add[root] %= (10 ** 9 + 7)
            return

        self.lazy_push_down(root, l, r)

        left = 2 * root + 1
        right = 2 * root + 2
        mid = (l + r) // 2
        if ul <= mid:
            self._add_update(left, l, mid, ul, ur, addval)
        if mid + 1 <= ur:
            self._add_update(right, mid + 1, r, ul, ur, addval)

        self.push_up(root, l, r)

    def _mul_update(self, root: int, l: int, r: int, ul: int, ur: int, mulval: int) -> None:
        if ul <= l and r <= ur:
            self.treesum[root] *= mulval
            self.mul[root] *= mulval
            self.add[root] *= mulval
            return

        self.lazy_push_down(root, l, r)

        left = 2 * root + 1
        right = 2 * root + 2
        mid = (l + r) // 2
        if ul <= mid:
            self._mul_update(left, l, mid, ul, ur, mulval)
        if mid + 1 <= ur:
            self._mul_update(right, mid + 1, r, ul, ur, mulval)

        self.push_up(root, l, r)

    def _query(self, root: int, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.treesum[root]

        self.lazy_push_down(root, l, r)

        left = 2 * root + 1
        right = 2 * root + 2
        mid = (l + r) // 2

        range_sum = self._query(left, l, mid, ql, qr) + self._query(right, mid + 1, r, ql, qr)
        return range_sum % (10 ** 9 + 7)


class Fancy_1622_奇妙序列_数组:

    def __init__(self):
        self.n = -1  # 实指 
        self.ST = tree_线段树_数组(10 ** 5)

    def append(self, val: int) -> None:
        self.n += 1
        self.ST.add_update(self.n, self.n, val)

    def addAll(self, inc: int) -> None:
        if self.n >= 0:  # 有个奇葩测试数据，上来就加
            self.ST.add_update(0, self.n, inc)

    def multAll(self, m: int) -> None:
        if self.n >= 0:
            self.ST.mul_update(0, self.n, m)

    def getIndex(self, idx: int) -> int:
        if self.n < idx:
            return -1
        return self.ST.query(idx, idx)




class Solution_699_掉落的方块(object):
    def fallingSquares(self, positions):
        coords = set()
        for left, size in positions:
            coords.add(left)
            coords.add(left + size - 1)
        index = {x: i for i, x in enumerate(sorted(coords))}

        tree = tree_线段树(len(index),update_fn=max,query_fn=max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            print(tree.lazy,tree.tree)
            best = max(best, h)
            ans.append(best)

        return ans
