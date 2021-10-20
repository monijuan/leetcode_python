# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 8:39
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 211. 添加与搜索单词 - 数据结构设计.py
# @Software: PyCharm
# ===================================
"""请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
 

示例：

输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

提示：

1 <= word.length <= 500
addWord 中的 word 由小写英文字母组成
search 中的 word 由 '.' 或小写英文字母组成
最多调用 50000 次 addWord 和 search

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-add-and-search-words-data-structure
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Trie:
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

    def search(self,word,index,node)->bool:
        if index==len(word):return node.isEnd
        if word[index] == '.':
            for child in node.children:
                if child is not None and self.search(word, index + 1, child):
                    return True
        else:
            child = node.children[ord(word[index]) - ord('a')]
            if child is not None and self.search(word, index + 1, child):
                return True
        return False

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word,0,self.trie)


def test(data_test):
    s = WordDictionary()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = WordDictionary(*data_test[1][0])
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
