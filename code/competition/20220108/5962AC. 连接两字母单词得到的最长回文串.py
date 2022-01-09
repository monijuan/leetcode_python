# -*- coding: utf-8 -*-
# @Time    : 2022/1/8 22:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5962AC. 连接两字母单词得到的最长回文串.py
# @Software: PyCharm 
# ===================================
"""给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。

请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。

请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。

回文串 指的是从前往后和从后往前读一样的字符串。



示例 1：

输入：words = ["lc","cl","gg"]
输出：6
解释：一个最长的回文串为 "lc" + "gg" + "cl" = "lcggcl" ，长度为 6 。
"clgglc" 是另一个可以得到的最长回文串。
示例 2：

输入：words = ["ab","ty","yt","lc","cl","ab"]
输出：8
解释：最长回文串是 "ty" + "lc" + "cl" + "yt" = "tylcclyt" ，长度为 8 。
"lcyttycl" 是另一个可以得到的最长回文串。
示例 3：

输入：words = ["cc","ll","xx"]
输出：2
解释：最长回文串是 "cc" ，长度为 2 。
"ll" 是另一个可以得到的最长回文串。"xx" 也是。


提示：

1 <= words.length <= 105
words[i].length == 2
words[i] 仅包含小写英文字母。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def longestPalindrome(self, words: List[str]) -> int:
        pairset = defaultdict(int)
        sameset = defaultdict(int)
        pairs = 0
        ps = []
        for w in words:
            ws = w[::-1]
            if w==ws:sameset[w]+=1  # aa
            else:   # ab
                if pairset[ws]>0:
                    pairset[ws]-=1
                    pairs+=1
                    ps.append((w,ws))
                else:
                    pairset[w]+=1
        res = 4*pairs
        od =  False
        print(ps)
        print(pairset)
        print(sameset)
        print(pairs)
        for numsame in sameset.values():
            if numsame>0:
                if numsame&1:
                    od=True
                    numsame-=1
                res += 2*numsame
        if od:res+=2
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.longestPalindrome(*data)


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
        # [["qo","fo","fq","qf","fo","ff","qq","qf","of","of","oo","of","of","qf","qf","of"]],# 14
        [["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')