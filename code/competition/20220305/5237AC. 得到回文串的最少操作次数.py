# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 22:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5237AC. 得到回文串的最少操作次数.py
# @Software: PyCharm 
# ===================================
"""给你一个只包含小写英文字母的字符串 s 。

每一次 操作 ，你可以选择 s 中两个 相邻 的字符，并将它们交换。

请你返回将 s 变成回文串的 最少操作次数 。

注意 ，输入数据会确保 s 一定能变成一个回文串。



示例 1：

输入：s = "aabb"
输出：2
解释：
我们可以将 s 变成 2 个回文串，"abba" 和 "baab" 。
- 我们可以通过 2 次操作得到 "abba" ："aabb" -> "abab" -> "abba" 。
- 我们可以通过 2 次操作得到 "baab" ："aabb" -> "abab" -> "baab" 。
因此，得到回文串的最少总操作次数为 2 。
示例 2：

输入：s = "letelt"
输出：2
解释：
通过 2 次操作从 s 能得到回文串 "lettel" 。
其中一种方法是："letelt" -> "letetl" -> "lettel" 。
其他回文串比方说 "tleelt" 也可以通过 2 次操作得到。
可以证明少于 2 次操作，无法得到回文串。


提示：

1 <= s.length <= 2000
s 只包含小写英文字母。
s 可以通过有限次操作得到一个回文串。
"""
from leetcode_python.utils import *

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        res=0
        n = len(s)
        s = list(s)
        s1 = s[::-1]
        for i in range(n // 2):
            if s[i:].count(s[i]) != 1:
                temp = s1[:n - i].index(s[i])
                s1.pop(temp)
                res += temp
                s = s1[::-1]
            else:
                res += n // 2 - i
                s[i] = None
                s1 = s[::-1]
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.minMovesToMakePalindrome(*data)


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
        ["letelt"],
        ["eqvvhtcsaaqtqesvvqch"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

