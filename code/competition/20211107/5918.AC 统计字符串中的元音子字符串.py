# -*- coding: utf-8 -*-
# @Time    : 2021/11/7 10:31
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5918.AC 统计字符串中的元音子字符串.py
# @Software: PyCharm 
# ===================================
"""子字符串 是字符串中的一个连续（非空）的字符序列。

元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。

给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。



示例 1：

输入：word = "aeiouu"
输出：2
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "aeiouu"
- "aeiouu"
示例 2：

输入：word = "unicornarihan"
输出：0
解释：word 中不含 5 种元音，所以也不会存在元音子字符串。
示例 3：

输入：word = "cuaieuouac"
输出：7
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
示例 4：

输入：word = "bbaeixoubb"
输出：0
解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。


提示：

1 <= word.length <= 100
word 仅由小写英文字母组成
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """AC"""
        pass

    def cnt(self,chars):
        """计算这个元音字串有多少符合条件的子串"""
        length = len(chars)
        if length<5 or len(set(chars))<5:return 0
        res = 0
        for first,char in enumerate(chars):
            last=first
            while last < length and len(set(chars[first:last]))<5:last+=1
            # print(chars,first,last,length-last)
            if 5==len(set(chars[first:last])):res += (length-last +1)

        return res


    def countVowelSubstrings(self, word: str) -> int:
        need = 'aeiou'
        res = 0
        startid,right=0,0
        length = len(word)
        for id,char in enumerate(word):
            if char in need and id<length-1:continue
            # if id>startid or id==length-1:
            endid = id if char not in need else id+1
            res+=self.cnt(word[startid:endid])
            startid = endid+1
            

        return res


def test(data_test):
    s = Solution()
    return s.countVowelSubstrings(*data_test)


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
        ["aeiouu"],
        ["unicornarihan"],
        ["cuaieuouac"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')