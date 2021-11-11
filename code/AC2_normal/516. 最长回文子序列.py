# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 10:32
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 516. 最长回文子序列.py
# @Software: PyCharm
# ===================================
"""给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

示例 1：

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。
示例 2：

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。
 

提示：

1 <= s.length <= 1000
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def longestPalindromeSubseq(self, s: str) -> int:
        res = self.longestCommonSubsequence_1143_最长公共子序列(s,s[::-1])
        return res

    def longestCommonSubsequence_1143_最长公共子序列(self, text1: str, text2: str) -> int:
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

def test(data_test):
    s = Solution()
    return s.longestPalindromeSubseq(*data_test)


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
