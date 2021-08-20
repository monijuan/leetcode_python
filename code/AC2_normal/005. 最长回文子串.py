# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 13:08
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 005. 最长回文子串.py
# @Software: PyCharm
# ===================================
"""给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 1: return s
        # 创建动态规划dynamic programing表
        dp = [[False for _ in range(length)] for _ in range(length)]
        # 初始长度为1，这样万一不存在回文，就返回第一个值（初始条件设置的时候一定要考虑输出）
        max_len = 1
        start = 0
        for right in range(1, length):
            for left in range(right):
                # 有两种情况是回文：如果是相邻两个数，相等即可；或者两头相等，去掉两头的中间是回文；
                if (right - left <= 2 and s[left] == s[right]) or (right - left > 2 and s[left] == s[right] and dp[left + 1][right - 1]):
                    dp[left][right] = True
                    if max_len < right - left + 1:  # 返回的是最长回文子串的第一个
                        max_len = right - left + 1
                        start = left
        return s[start:start + max_len]


def test(data_test):
    s = Solution()
    return s.longestPalindrome(*data_test)

if __name__ == '__main__':
    datas = [
        ["babad"],  # bab
        ["cbbd"],  # bb
        ["a"],  # a
        ["ac"],  # a
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
