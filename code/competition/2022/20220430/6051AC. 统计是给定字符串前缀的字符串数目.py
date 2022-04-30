# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 21:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6051AC. 统计是给定字符串前缀的字符串数目.py
# @Software: PyCharm 
# ===================================
"""给你一个字符串数组 words 和一个字符串 s ，其中 words[i] 和 s 只包含 小写英文字母 。

请你返回 words 中是字符串 s 前缀 的 字符串数目 。

一个字符串的 前缀 是出现在字符串开头的子字符串。子字符串 是一个字符串中的连续一段字符序列。



示例 1：

输入：words = ["a","b","c","ab","bc","abc"], s = "abc"
输出：3
解释：
words 中是 s = "abc" 前缀的字符串为：
"a" ，"ab" 和 "abc" 。
所以 words 中是字符串 s 前缀的字符串数目为 3 。
示例 2：

输入：words = ["a","a"], s = "aa"
输出：2
解释：
两个字符串都是 s 的前缀。
注意，相同的字符串可能在 words 中出现多次，它们应该被计数多次。


提示：

1 <= words.length <= 1000
1 <= words[i].length, s.length <= 10
words[i] 和 s 只 包含小写英文字母。
"""
from leetcode_python.utils import *

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(w) for w in  words)


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countPrefixes(*data)

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
        [["a","b","c","ab","bc","abc"],"abc"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
