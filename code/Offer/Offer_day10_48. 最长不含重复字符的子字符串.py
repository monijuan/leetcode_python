# -*- coding: utf-8 -*-
# @Time    : 2021/9/3 10:53
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day10_48. 最长不含重复字符的子字符串.py
# @Software: PyCharm
# ===================================
"""请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

s.length <= 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        lengths = 0
        for right,char in enumerate(s):
            char_in_id = s[left:right].find(char)
            if 0<=char_in_id: left+=char_in_id+1
            lengths=max(right-left+1,lengths)

        return lengths


def test(data_test):
    s = Solution()
    return s.lengthOfLongestSubstring(*data_test)


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
        ["abcabcbb"],
        ["bbbbb"],
        ["pwwkew"],
        ["pwwshaioduhsaojdlqwperiqphosxcklnvlkasdlqwsadqwepaslkxcznoaherierqpwjeupqwjeqwrkew"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
