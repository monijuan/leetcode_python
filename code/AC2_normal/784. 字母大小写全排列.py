# -*- coding: utf-8 -*-
# @Time    : 2021/10/22 15:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 784. 字母大小写全排列.py
# @Software: PyCharm
# ===================================
"""给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

 

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
 

提示：

S 的长度不超过12。
S 仅由数字和字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        self.res = []

    def change(self,s_left,changeindex):
        """逐个字符判断，如果是数字就继续，如果是字母则分叉进行下一步"""
        if changeindex==self.length:
            self.res.append(s_left)
        else:
            char = self.s[changeindex]
            if char.isnumeric():
                self.change(s_left + char,changeindex+1)
            else:
                self.change(s_left + char.upper(),changeindex+1)
                self.change(s_left + char.lower(),changeindex+1)

    def letterCasePermutation(self, s: str) -> List[str]:
        self.s = s
        self.length = len(s)
        self.change('',0)
        return self.res


def test(data_test):
    s = Solution()
    return s.letterCasePermutation(*data_test)


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
