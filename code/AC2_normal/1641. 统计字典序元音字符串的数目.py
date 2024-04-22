# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 9:11
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1641. 统计字典序元音字符串的数目.py
# @Software: PyCharm
# ===================================
"""给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。

字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

 

示例 1：

输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]
示例 2：

输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
示例 3：

输入：n = 33
输出：66045
 

提示：

1 <= n <= 50 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-sorted-vowel-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def countVowelStrings(self, n: int) -> int:
        a=e=i=o=u=1
        n-=1
        while n:
            aa=a+e+i+o+u
            ee=e+i+o+u
            ii=i+o+u
            oo=o+u
            a,e,i,o = aa,ee,ii,oo
            n-=1
        return a+e+i+o+u

class Solution2:
    def countVowelStrings(self, n: int) -> int:
        """
        等价于：把aeiou看成是一个队伍的五个小组，队伍长度为n，相当于算有多少分组方法，每组可以为空
        又等价于：队伍长度为n+5，中间放四个隔板切成五个小组，隔板是在n+4个位置中选四个
        """
        return int((n + 1) * (n + 2) * (n + 3) * (n + 4) / 24)

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countVowelStrings(*data)


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
        [1],
        [2],
        [33],
        [50],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
