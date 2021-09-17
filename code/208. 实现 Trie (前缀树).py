# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 9:12
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 208. 实现 Trie (前缀树).py
# @Software: PyCharm
# ===================================
"""Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
 

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def __searchPrefix(self,prefix:str)->"Trie":
        node = self
        for char in prefix:
            char_int = ord(char)-ord('a')
            if node.children[char_int] is None:return None
            node = node.children[char_int]
        return node

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            char_int = ord(char)-ord('a')
            if node.children[char_int] is None:
                node.children[char_int] = Trie()
            node = node.children[char_int]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """判断是否有这个单词，需要找到 word 是前缀，并且到这个 word 结束了"""
        node = self.__searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        """判断有没有prefix的单词"""
        return self.__searchPrefix(prefix) is not None


def test(data_test):
    s = Trie()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = Trie(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [["Trie","insert","search","search","startsWith","insert","search"],
         [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
