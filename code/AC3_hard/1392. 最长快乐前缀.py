# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 16:04
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1392. 最长快乐前缀.py
# @Software: PyCharm
# ===================================
"""「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。

给你一个字符串 s，请你返回它的 最长快乐前缀。

如果不存在满足题意的前缀，则返回一个空字符串。

 

示例 1：

输入：s = "level"
输出："l"
解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
示例 2：

输入：s = "ababab"
输出："abab"
解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
示例 3：

输入：s = "leetcodeleet"
输出："leet"
示例 4：

输入：s = "a"
输出：""
 

提示：

1 <= s.length <= 10^5
s 只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-happy-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        参考官解：https://leetcode-cn.com/problems/longest-happy-prefix/solution/zui-chang-kuai-le-qian-zhui-by-leetcode-solution/
        prefix，最后多新字符就相当于原编码值乘以 base 再加上新的字符的编码值；
        suffix，最前多新字符就相当于原编码值加上新的字符的编码值乘以 base 的 i-1 次幂。
        """
        pass

    def longestPrefix(self, s: str) -> str:
        length = len(s)
        prefix=suffix=index=0
        base,mod,mul,a = 31,10**9+7,1,ord('a')
        for i in range(0,length-1):
            prefix = (prefix*base + ord(s[i]) - a) % mod
            suffix = (suffix + (ord(s[length - i-1]) - a)*mul) % mod
            if prefix == suffix:index = i+1
            mul = (mul*base)%mod
        return s[:index]


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.longestPrefix(*data)


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
        ["leetcodeleet"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
