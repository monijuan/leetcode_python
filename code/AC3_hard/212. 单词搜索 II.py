# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 9:08
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 212. 单词搜索 II.py
# @Software: PyCharm
# ===================================
"""给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

 

示例 1：


输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]
示例 2：


输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]
 

提示：

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        self.word = ''

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            char_int = ord(char)-ord('a')
            if node.children[char_int] is None:
                node.children[char_int] = Trie()
            node = node.children[char_int]
        node.isEnd = True
        node.word = word


class Solution:
    def __init__(self):
        self.trie = Trie()
        self.res = set()    # word去重

    def __dfs(self,now,row_id,col_id):
        print(f'dfs:{row_id},{col_id},{now.word}')
        char = self.board[row_id][col_id]
        char_int = ord(char)-ord('a')
        if char_int not in now.children:return
        if now.word!='':self.res.add(now.word)

        self.board[row_id][col_id]='#'
        for row_id,col_id in [(row_id+1,col_id),(row_id-1,col_id),(row_id,col_id+1),(row_id,col_id-1)]:
            if 0<=row_id<self.height and 0<=col_id<self.width:
                self.__dfs(now,row_id,col_id)
        self.board[row_id][col_id]=char


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.height = len(board)
        self.width = len(board[0])
        self.board = board

        for word in words:
            self.trie.insert(word)

        for row_id in range(self.height):
            for col_id in range(self.width):
                self.__dfs(self.trie,row_id,col_id)

        return list(self.res)

def test(data_test):
    s = Solution()
    return s.findWords(*data_test)

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
        [[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]],
        # [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
