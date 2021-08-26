# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 17:22
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : Offer_day03_05. 替换空格.py
# @Software: PyCharm
# ===================================
"""请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def replaceSpace(self, s: str) -> str:
        s = s.replace(' ','%20')
        return s


def test(data_test):
    s = Solution()
    return s.replaceSpace(*data_test)


if __name__ == '__main__':
    datas = [
        ["We are happy."],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
