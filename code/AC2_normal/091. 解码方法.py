# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 16:48
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 091. 解码方法.py
# @Software: PyCharm
# ===================================
"""一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

 

示例 1：

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2：

输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
示例 3：

输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
示例 4：

输入：s = "06"
输出：0
解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。
 

提示：

1 <= s.length <= 100
s 只包含数字，并且可能包含前导零。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def numDecodings(self, s: str) -> int:
        if '0'==s[0]:return 0
        dp_self = 1
        dp_second = 0
        for index in range(1,len(s)):
            dp_self_last = dp_self
            dp_second_last = dp_second
            if '0' == s[index]:
                dp_self = 0
            else:
                dp_self = dp_self_last + dp_second_last

            if '10' <= s[index - 1:index + 1] <= '26':
                dp_second = dp_self_last
            else:
                dp_second = 0

        return dp_self+dp_second

    def numDecodings_639_解码方法2(self, s:str) -> int:
        if '0'==s[0]:return 0
        dp_self = 1 if s[0]!='*' else 9
        dp_second = 0
        for index in range(1,len(s)):
            char_left = s[index-1]
            char = s[index]
            dp_self_last = dp_self
            dp_second_last = dp_second
            # dp_self
            if '0' == char:
                dp_self = 0
            else:
                dp_self = (dp_self_last+dp_second_last) * (9 if s[index]=='*' else 1)

            # dp_second
            if '*' == char_left:
                if char == '*':
                    dp_second = dp_self_last // 9 * 15 # /9*15  (11~19,21~26)
                elif char <'7':
                    dp_second = dp_self_last // 9 * 2  # /9*2 (1x,2x)
                else:
                    dp_second = dp_self_last // 9 # /9*1 (1x)
            elif '1'==char_left:
                dp_second = dp_self_last * (9 if char=='*' else 1) # 1x
            elif '2'==char_left and char not in '789':
                dp_second = dp_self_last * (6 if char=='*' else 1)
            else: # (char_left in '03456789') or ('2'==char_left and char in '789')
                dp_second = 0
        print(dp_self)
        print(dp_second)
        return (dp_self+dp_second)%(10**9+7)


def test(data_test):
    s = Solution()
    return s.numDecodings(*data_test)


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
