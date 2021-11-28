# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 9:50
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-001. 小美的用户名.py
# @Software: PyCharm
# ===================================
"""小美是美团的前端工程师，为了防止系统被恶意攻击，小美必须要在用户输入用户名之前做一个合法性检查，一个合法的用户名必须满足以下几个要求：

用户名的首字符必须是大写或者小写字母。
用户名只能包含大小写字母，数字。
用户名需要包含至少一个字母和一个数字。
如果用户名合法，请输出 "Accept"，反之输出 "Wrong"。
格式：


输入：
- 输入第一行包含一个正整数 T，表示需要检验的用户名数量。
- 接下来有 T 行，每行一个字符串 s，表示输入的用户名。
输出：
- 对于每一个输入的用户名 s，请输出一行，即按题目要求输出一个字符串。
示例：


输入：
     5
     Ooook
     Hhhh666
     ABCD
     Meituan
     6666
输出：
     Wrong
     Accept
     Wrong
     Wrong
     Wrong
提示：

1 <= T <= 100
s 的长度不超过 20
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/BaR9fy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

def check(name):
    if not name[0].isalpha():return False   # 排除首字母不是英文
    elif name.isalpha():return False    # 排除纯字母
    else: return name.isalnum() # 排除其它字符

T = int(input())
while T:
    print('Accept' if check(str(input())) else 'Wrong')
