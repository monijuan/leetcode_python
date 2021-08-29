# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 9:27
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 443. 压缩字符串.py
# @Software: PyCharm
# ===================================
"""给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

 

示例 1：

输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
示例 2：

输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。
示例 3：

输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：
由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
注意每个数字在数组中都有它自己的位置。
 

提示：

1 <= chars.length <= 2000
chars[i] 可以是小写英文字母、大写英文字母、数字或符号

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-compression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List

class Solution:
    def __init__(self):
        pass

    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        id_char_start = 0
        left,right=0,0
        while id_char_start<length:
            right = id_char_start  # id_char_start 到 right-1 都是同一个字母
            while right<length and chars[right]==chars[id_char_start]:
                right+=1
            chars[left]=chars[id_char_start]
            left+=1
            if right-id_char_start>1:
                for char in str(right-id_char_start):
                    chars[left]=char
                    left+=1
            id_char_start = right   # right开始是另一个字母
        # chars = chars[:left]
        return left

    def compress_for(self, chars: List[str]) -> int:
        """没办法顾及最后一项，如果要用for还要区分最后一个是一样的还是不一样的。"""
        length = len(chars)
        next_char = chars[0]
        # count = 0
        left = 0
        id_start=0
        for right in range(length):
            if next_char!=chars[right] or right==length-1:
                # pass
            # else:# right 和之前的不一样
                chars[left] = next_char
                left+=1
                next_char = chars[right]

                count = right - id_start if right<length-1 else right - id_start+1
                id_start = right
                if count>1:
                    for char_c in str(count):
                        chars[left]=char_c
                        left+=1
            # print(chars,f'i={left}, j={right}, id_start={id_start}')
        chars = chars[:left]
        print('res=',chars,left)
        return left


def test(data_test):
    s = Solution()
    return s.compress(*data_test)
    # return s.compress2(*data_test)

if __name__ == '__main__':
    datas = [
        # [["a","a","b","b","c","c","c"]],    # 6
        [["a"]],    # 1
        # [["a","b","b","b","b","b","b","b","b","b","b","b","b"]],    # 4
        # [["a","b","b","b","b","b","b","b","b","b","b","b","b","c"]],    # 4
        [["a","b","b","b","c","c","c","c","b","c","c","c","c","c","c","c","c","c","c","c","c","b","b","b","b","b","b","b","b","b","b","b","b"]],    # 4
        # [["a","b","c"]],    # ["a","b","c"]
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')