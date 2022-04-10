# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 8:59
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6033AC. 转换数字的最少位翻转次数.py
# @Software: PyCharm 
# ===================================
"""一次 位翻转 定义为将数字 x 二进制中的一个位进行 翻转 操作，即将 0 变成 1 ，或者将 1 变成 0 。

比方说，x = 7 ，二进制表示为 111 ，我们可以选择任意一个位（包含没有显示的前导 0 ）并进行翻转。比方说我们可以翻转最右边一位得到 110 ，或者翻转右边起第二位得到 101 ，或者翻转右边起第五位（这一位是前导 0 ）得到 10111 等等。
给你两个整数 start 和 goal ，请你返回将 start 转变成 goal 的 最少位翻转 次数。

 

示例 1：

输入：start = 10, goal = 7
输出：3
解释：10 和 7 的二进制表示分别为 1010 和 0111 。我们可以通过 3 步将 10 转变成 7 ：
- 翻转右边起第一位得到：1010 -> 1011 。
- 翻转右边起第三位：1011 -> 1111 。
- 翻转右边起第四位：1111 -> 0111 。
我们无法在 3 步内将 10 转变成 7 。所以我们返回 3 。
示例 2：

输入：start = 3, goal = 4
输出：3
解释：3 和 4 的二进制表示分别为 011 和 100 。我们可以通过 3 步将 3 转变成 4 ：
- 翻转右边起第一位：011 -> 010 。
- 翻转右边起第二位：010 -> 000 。
- 翻转右边起第三位：000 -> 100 。
我们无法在 3 步内将 3 变成 4 。所以我们返回 3 。
 

提示：

0 <= start, goal <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-bit-flips-to-convert-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start^goal).bit_count()


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
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
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
