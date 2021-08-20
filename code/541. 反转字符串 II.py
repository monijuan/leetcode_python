# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 10:40
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 541. 反转字符串 II.py
# @Software: PyCharm
# ===================================
"""给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
 

示例 1：

输入：s = "abcdefg", k = 2
输出："bacdfeg"
示例 2：

输入：s = "abcd", k = 2
输出："bacd"
 

提示：

1 <= s.length <= 104
s 仅由小写英文组成
1 <= k <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        """2k，2k往前，每次拼接【前k反转】和【后k】，最后的一组用min限制"""
        pass

    def reverseStr(self, s: str, k: int) -> str:
        res = ''
        length = len(s)
        for time in range(length//(2*k)+1):
            start = time*2*k
            mid = min(start+k,length)
            end = min(mid+k,length)
            res = res + ''.join(reversed(s[start:mid])) + s[mid:end]
        return res

def test(data_test):
    s = Solution()
    return s.reverseStr(*data_test)


if __name__ == '__main__':
    datas = [
        # ['abcdefg',2],      # bacdfeg
        ['abcdefgqwgheohqwoieqwhoi',2],
        ['abcdefgqwgheohqwoieqwhoi',11111],
        # ['abcd',2],     # bacd
        # ['a',2],
        # ['',2],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
