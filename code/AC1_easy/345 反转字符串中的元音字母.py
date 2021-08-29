# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 13:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 345 反转字符串中的元音字母.py
# @Software: PyCharm
# ===================================
"""给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。

示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"
 

提示：

1 <= s.length <= 3 * 105
s 由 可打印的 ASCII 字符组成

"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        length = len(s)
        left, right = 0, length-1
        元音 = ['a','e','i','o','u']

        while left<right:
            while left<length and chars[left].lower() not in 元音:
                left+=1
            while 0<right and chars[right].lower() not in 元音:
                right-=1
            # print(left,right)
            if left<right:
                t = chars[left]
                chars[left] = chars[right]
                chars[right] = t
                left+=1
                right-=1
        return ''.join(chars)


def test(data_test):
    s = Solution()
    return s.reverseVowels(data_test)


if __name__ == '__main__':
    datas = [
        'hello',
        'leetcode',
        'aA',
        '.,',
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
