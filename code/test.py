# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 16:01
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : test.py
# @Software: PyCharm
# ===================================
from leetcode_python.utils import *

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


def test():
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
