# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 8:59
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 524. 通过删除字母匹配到字典里最长单词.py
# @Software: PyCharm
# ===================================
"""给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。

如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。

 

示例 1：

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
示例 2：

输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
 

提示：

1 <= s.length <= 1000
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 1000
s 和 dictionary[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import re

from leetcode_python.utils import *


class Solution:
    def __init__(self):
        import re
        """
        ["abce",["abe","abc"]] 的结果是 "abc"就很迷
        """
        pass

    def isMatch(self,word:str)->bool:
        i=0
        for char in word:
            while i<self.length and char!= self.s[i]:
                i+=1
            if i==self.length :return False
            else:i+=1
        return True

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ''
        self.s = s
        self.length = len(s)
        for word in dictionary:
            if self.isMatch(word) and (len(res)<len(word) or (len(res)==len(word) and res>word)):
                res = word
        return res


    def findLongestWord_超时(self, s: str, dictionary: List[str]) -> str:
        res = ''
        for x in dictionary:
            if re.search('.*'.join(x),s) and (len(res)<len(x) or (len(res)==len(x) and res>x)):
                res = x
        return res


def test(data_test):
    s = Solution()
    return s.findLongestWord(*data_test)


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
        # ["abpcplea", ["ale","apple","monkey","plea"]],
        # ["abce",["abe","abc"]],
        ["bab", ["ba","ab","a","b"]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
