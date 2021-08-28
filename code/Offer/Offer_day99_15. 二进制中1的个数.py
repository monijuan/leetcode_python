# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 20:22
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : Offer_day99_15. 二进制中1的个数.py
# @Software: PyCharm
# ===================================
"""编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

 

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用 二进制补码 记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List
# 本题与主站 191 题相同

class Solution:
    def __init__(self):
        pass

    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            if n & 1:cnt+=1
            n//=2
        return cnt


def test(data_test):
    s = Solution()
    return s.hammingWeight(*data_test)

if __name__ == '__main__':
    datas = [
        [11],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')