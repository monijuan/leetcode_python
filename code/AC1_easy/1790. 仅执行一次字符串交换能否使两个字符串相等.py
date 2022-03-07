# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 16:18
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1790. 仅执行一次字符串交换能否使两个字符串相等.py
# @Software: PyCharm
# ===================================
"""给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。

 

示例 1：

输入：s1 = "bank", s2 = "kanb"
输出：true
解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"
示例 2：

输入：s1 = "attack", s2 = "defend"
输出：false
解释：一次字符串交换无法使两个字符串相等
示例 3：

输入：s1 = "kelb", s2 = "kelb"
输出：true
解释：两个字符串已经相等，所以不需要进行字符串交换
示例 4：

输入：s1 = "abcd", s2 = "dcba"
输出：false
 

提示：

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 和 s2 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):return False
        ss1,ss2 = [],[]
        for a,b in zip(s1,s2):
            if a!=b:
                ss1.append(a)
                ss2.append(b)
        if len(ss1)==0:return True
        if len(ss1)!=2:return False
        a1,b1=ss1
        a2,b2=ss2
        return a1==b2 and a2==b1


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
