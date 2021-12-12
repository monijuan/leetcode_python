# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 16:01
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : test.py
# @Software: PyCharm
# ===================================
from leetcode_python.utils import *

def test():
    li = list(range(3))
    n, d = len(li), defaultdict(set)
    for i, j, k in product(range(n), repeat = 3):
        print(i,j,k)

# 212
"""
from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word: cur = cur.children[c]
        cur.is_word = True
        cur.word = word

class Solution:
    def __init__(self):
        self.res = set()

    def dfs(self, now, i1, j1):
        if self.board[i1][j1] not in now.children:return
        ch = self.board[i1][j1]
        now = now.children[ch]
        if now.word != "":self.res.add(now.word)
        self.board[i1][j1] = "#"
        for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
            if 0 <= i2 < self.height and 0 <= j2 < self.width:
                self.dfs(now, i2, j2)
        self.board[i1][j1] = ch

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        trie = Trie()
        for word in words: trie.insert(word)
        for i in range(self.height):
            for j in range(self.width):
                self.dfs(trie, i, j)

        return list(self.res)
"""
###
def test7():
    import collections

    MOD = 10 ** 9 + 7

    # ------------------------输入，建图-------------------------#
    # ----结点个数，级别范围
    n, k = map(int, input().split())

    # ----建图。邻接表（链接矩阵也可以）
    adjvex = collections.defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        x -= 1  # 结点ID号统一成从0开始
        y -= 1
        adjvex[x].append(y)
        adjvex[y].append(x)

    # ----结点的级别
    rank = [int(x) for x in input().split()]

    # -----------------------尝试每个点--------------------------#
    min_rank = -1
    max_rank = -1
    root = -1  # 回溯时的基准root结点，方便比较，防止重复

    def backtrace(x: int) -> int:
        if not (min_rank <= rank[x] <= max_rank):
            return 0
        if x < root:
            return 0
        cnt = 1
        visited[x] = True
        for y in adjvex[x]:
            if visited[y] == False:
                cnt_old = cnt
                cnt = cnt * (backtrace(y) + 1) % MOD
        visited[x] = False

        return cnt

    visited = [False for _ in range(n)]
    res = 0
    for x in range(n):
        visited[x] = True
        min_rank = rank[x]  # 最低的级别
        max_rank = rank[x] + k  # 最高的级别
        root = x  # 标记，防止重复
        backtrace_x = backtrace(x)
        print(x+1,backtrace_x)
        res += backtrace_x
        res %= MOD
        visited[x] = False
    print(res)

def test6():
    li = [0,1]*2
    li[0]=2
    print(li)

def test5():
    print(2**10)

def test4():
    chars = '()*'

    length = 100
    times = 10
    while times:
        times-=1
        str = ''
        for x in range(length):
            str+=chars[random.randint(0, 2)]
        print(f'"{str}"')


def test3():
    n=10

    for i in range(n):
        print('-'*50)
        print(f'i={i}')
        times = 0
        for w in range(1,n,2):
            time = min(i+1,n-i,w,(n-1)//2)
            times+=time
            print(f'i:{i}, w:{w}, time:{time}')
        print(f'[res]n:{n}, i:{i}, times:{times}')

def test2():
    res = 11 & 1
    res = 12 & 1
    print(res)

def test1():
    for x in range(50000,50200):
        print(f'[{x}],',end='')
    print()
    for x in range(50000,50200):
        print(f',"addNum"',end='')
    return


if __name__ == '__main__':
    test()
