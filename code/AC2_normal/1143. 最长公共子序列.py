# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 8:06
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1143. 最长公共子序列.py
# @Software: PyCharm 
# ===================================
"""给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

 

示例 1：

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
示例 2：

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
示例 3：

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
 

提示：

1 <= text1.length, text2.length <= 1000
text1 和 text2 仅由小写英文字符组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length1,length2 = len(text1),len(text2)
        if 0==length1 and 0==length2:return 0
        this_dp = [0]*(length1+1)
        for to_word2 in range(length2+1):
            last_dp = this_dp.copy()
            for from_word1 in range(length1+1):
                if 0==from_word1 or 0==to_word2:
                    this_dp[from_word1] = 0
                elif text1[from_word1-1]==text2[to_word2-1]:
                    this_dp[from_word1] = last_dp[from_word1-1] + 1
                else:
                    this_dp[from_word1] = max(this_dp[from_word1 - 1], last_dp[from_word1])
            print(f'to w2[{to_word2}-1], {this_dp}')
        return this_dp[-1]


    def minDistance_583_两个字符串的删除操作(self, word1: str, word2: str) -> int:
        length1,length2 = len(word1),len(word2)
        if 0==length1 and 0==length2:return 0
        this_dp = [0]*(length1+1) # word1 的每个字母到 word2 每个字母需要删除的次数
        for to_word2 in range(length2+1):
            last_dp = this_dp.copy()
            for from_word1 in range(length1+1):
                if 0==from_word1 or 0==to_word2:   # 考虑word1删到0的情况
                    this_dp[from_word1] = from_word1 + to_word2
                elif word1[from_word1-1]==word2[to_word2-1]:
                    this_dp[from_word1] = last_dp[from_word1-1]
                else:
                    this_dp[from_word1] = min(this_dp[from_word1 - 1], last_dp[from_word1]) + 1
            print(f'to w2[{to_word2}-1], {this_dp}')
        return this_dp[-1]

def test(data_test):
    s = Solution()
    return s.longestCommonSubsequence(*data_test)


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
        ["abcde","ace"],
        ["abc","abc"],
        ["abc","def"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')