# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 11:08
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5919AC. 所有子字符串中的元音.py
# @Software: PyCharm 
# ===================================
"""给你一个字符串 word ，返回 word 的所有子字符串中 元音的总数 ，元音是指 'a'、'e'、'i'、'o' 和 'u' 。

子字符串 是字符串中一个连续（非空）的字符序列。

注意：由于对 word 长度的限制比较宽松，答案可能超过有符号 32 位整数的范围。计算时需当心。



示例 1：

输入：word = "aba"
输出：6
解释：
所有子字符串是："a"、"ab"、"aba"、"b"、"ba" 和 "a" 。
- "b" 中有 0 个元音
- "a"、"ab"、"ba" 和 "a" 每个都有 1 个元音
- "aba" 中有 2 个元音
因此，元音总数 = 0 + 1 + 1 + 1 + 1 + 2 = 6 。
示例 2：

输入：word = "abc"
输出：3
解释：
所有子字符串是："a"、"ab"、"abc"、"b"、"bc" 和 "c" 。
- "a"、"ab" 和 "abc" 每个都有 1 个元音
- "b"、"bc" 和 "c" 每个都有 0 个元音
因此，元音总数 = 1 + 1 + 1 + 0 + 0 + 0 = 3 。
示例 3：

输入：word = "ltcd"
输出：0
解释："ltcd" 的子字符串均不含元音。
示例 4：

输入：word = "noosabasboosa"
输出：237
解释：所有子字符串中共有 237 个元音。


提示：

1 <= word.length <= 105
word 由小写英文字母组成
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        对下标为 id 的而言，左边有 id 个字母，右边有 length-id-1 个字母
            对左边的而言，这个字母会被调用 length-id 次，共 id*(length-id) 次
            对自己而言，这个字母可以作为开头有 length-id 个子串
            对右边的而言，这个字母会被调用 0 次
        因此，对于 id 而言，一共出现了 (id+1)*(length-id) 次
        所以，只要计算所有元音，各自出现在多少子串里
        AC
        """
        pass

    def countVowels(self, word: str) -> int:
        length = len(word)
        need = 'aeiou'
        res = 0
        for id,char in enumerate(word):
            if char in need:
                res += ((id+1)*(length-id))
        return res


def test(data_test):
    s = Solution()
    return s.countVowels(*data_test)


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
        ["aba"],
        ["abc"],
        ["ltcd"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')