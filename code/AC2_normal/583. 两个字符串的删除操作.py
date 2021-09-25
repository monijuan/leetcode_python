# -*- coding: utf-8 -*-
# @Time    : 2021/9/25 6:56
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 583. 两个字符串的删除操作.py
# @Software: PyCharm 
# ===================================
"""给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

 

示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
 

提示：

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def minDistance(self, word1: str, word2: str) -> int:
        length1,length2 = len(word1),len(word2)
        if 0==length1 and 0==length2:return 0
        this_dp = [0]*(length1+1) # word1 的每个字母到 word2 每个字母需要删除的次数
        for to_word2 in range(length2+1):
            last_dp = this_dp.copy()
            for from_word1 in range(length1+1):
                if 0==from_word1 or 0==to_word2:   # 考虑word1删到0的情况
                    this_dp[from_word1] = from_word1 + to_word2
                elif word1[from_word1-1]==word2[to_word2-1]:
                    this_dp[from_word1] = last_dp[from_word1-1]
                else:
                    this_dp[from_word1] = min(this_dp[from_word1 - 1], last_dp[from_word1]) + 1
            print(f'to w2[{to_word2}-1], {this_dp}')
        return this_dp[-1]



def test(data_test):
    s = Solution()
    return s.minDistance(*data_test)


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
        ["sea","eat"],
        ["leetcode","etco"],
        # ["seat","qqqqeat"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')