# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 11:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-013. 偏爱字母.py
# @Software: PyCharm
# ===================================
"""小美喜欢字母 E ，讨厌字母 F 。在小美生日时，小团送了小美一个仅包含字母 E 和 F 的字符串，小美想从中选出一个包含字母 E 数量与字母 F 数量之差最大的子串。
*子串：从字符串前面连续删去若干个字符，从后面连续删去若干个字符剩下的字符串（也可以一个都不删），例如 abcab 是 fabcab 的子串，而不是 abcad 的子串。我们将空串看作所有字符串的子串。

格式：


输入：
- 第一行一个正整数 n 表示字符串的长度。
- 第二行长度为 n ，且仅包含大写字母 'E', 'F' 的字符串（不含引号）
输出：
- 输出一个整数，表示最大的差值。
示例：


输入：
     5
     EFEEF
输出：2
解释：
选择子串 EE ，此时有 2 个 E ，0 个 F ，有最大差值 2-0=2
另外，选择子串 EFEE 也可以达到最大差值。
提示：

对于 30% 的数据，n <= 300
对于 60% 的数据，n <= 3000
对于 100% 的数据，n <= 300000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pedXtA
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

_ = input()
s = input()
res, cnt = 0, 0
for c in s:
    if c == 'E':
        cnt += 1
        res = max(res, cnt)
    else:
        cnt -= 1
        cnt = max(cnt, 0)
print(res)