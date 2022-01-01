# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 9:02
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 472. 连接词.py
# @Software: PyCharm
# ===================================
"""给你一个 不含重复 单词的字符串数组 words ，请你找出并返回 words 中的所有 连接词 。

连接词 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。

 

示例 1：

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成;
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成;
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。
示例 2：

输入：words = ["cat","dog","catdog"]
输出：["catdog"]
 

提示：

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] 仅由小写字母组成
0 <= sum(words[i].length) <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/concatenated-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Trie_char:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            char_int = ord(char)-ord('a')
            if node.children[char_int] is None:
                node.children[char_int] = Trie()
            node = node.children[char_int]
        node.isEnd = True

    def dfs(self, word: str,start:int) -> bool:
        if start==len(word):return True
        node = self
        for i in range(start,len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:return False
            if node.isEnd and self.dfs(word,i+1):return True
        return False

class Trie:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.isEnd = True

    def dfs(self, word: str,start:int) -> bool:
        if start==len(word):return True
        node = self
        for i in range(start,len(word)):
            node = node.children.get(word[i],None)
            if node is None:return False
            if node.isEnd and self.dfs(word,i+1):return True
        return False



class Solution:
    def __init__(self):
        pass

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []
        root = Trie()
        for word in words:
            if word=='':continue
            if root.dfs(word,0):res.append(word)
            else:root.insert(word)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
