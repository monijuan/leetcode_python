# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 8:09
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 639.解码方法 II.py
# @Software: PyCharm
# ===================================
"""一条包含字母 A-Z 的消息通过以下的方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：

"AAJF" 对应分组 (1 1 10 6)
"KJF" 对应分组 (11 10 6)
注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。

除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串 "1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息。

给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。

由于答案数目可能非常大，返回对 109 + 7 取余 的结果。

 

示例 1：

输入：s = "*"
输出：9
解释：这一条编码消息可以表示 "1"、"2"、"3"、"4"、"5"、"6"、"7"、"8" 或 "9" 中的任意一条。
可以分别解码成字符串 "A"、"B"、"C"、"D"、"E"、"F"、"G"、"H" 和 "I" 。
因此，"*" 总共有 9 种解码方法。
示例 2：

输入：s = "1*"
输出：18
解释：这一条编码消息可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条。
每种消息都可以由 2 种方法解码（例如，"11" 可以解码成 "AA" 或 "K"）。
因此，"1*" 共有 9 * 2 = 18 种解码方法。
示例 3：

输入：s = "2*"
输出：15
解释：这一条编码消息可以表示 "21"、"22"、"23"、"24"、"25"、"26"、"27"、"28" 或 "29" 中的任意一条。
"21"、"22"、"23"、"24"、"25" 和 "26" 由 2 种解码方法，但 "27"、"28" 和 "29" 仅有 1 种解码方法。
因此，"2*" 共有 (6 * 2) + (3 * 1) = 12 + 3 = 15 种解码方法。
 

提示：

1 <= s.length <= 105
s[i] 是 0 - 9 中的一位数字或字符 '*'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-ways-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def numDecodings(self, s:str) -> int:
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
    
    def numDecodings_超时(self, s:str) -> int:
        if '0'==s[0]:return 0
        length = len(s)
        dp_self = [0]*length
        dp_second = [0]*length
        dp_self[0]=1 if s[0]!='*' else 9
        for index in range(1,length):
            char_left = s[index-1]
            char = s[index]
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
                dp_second = dp_self[index - 1] * (6 if char=='*' else 1)
            else: # (char_left in '03456789') or ('2'==char_left and char in '789')
                dp_second = 0
        print(dp_self)
        print(dp_second)
        return (dp_self[-1]+dp_second[-1])%(10**9+7)


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
        # ["*"],
        # ["1*"],
        # ["2*"],
        # ["*0*"],
        # ["*1*6"],
        # ["0*1*8"],
        # ["*1*65131*0**0*1*"],
        ["********"],
        ["*********"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
