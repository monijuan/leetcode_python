# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 16:13
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 187. 重复的DNA序列.py
# @Software: PyCharm
# ===================================
"""所有 DNA 都由一系列缩写为 'A'，'C'，'G' 和 'T' 的核苷酸组成，例如："ACGAATTCCG"。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来找出所有目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

 

示例 1：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]
示例 2：

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]
 

提示：

0 <= s.length <= 105
s[i] 为 'A'、'C'、'G' 或 'T'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def str2num(self,str):
        char2num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        num = 0
        for s in str:
            num = num*4+char2num[s]
        return num

    def num2str(self,num):
        num2char = {0:'A', 1:'C', 2:'G', 3:'T'}
        res = ''
        while num:
            res = num2char[num%4] + res
            num//=4
        res = 'A'*(10-len(res)) + res
        return res



    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        if length<=10:return []
        num_res = []
        num_set = set()
        char2num = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        num = 0
        for i in range(10):
            num = num*4+char2num[s[i]]
        num_set.add(num)
        for i in range(10,length):
            num = 4*(num - char2num[s[i-10]]*262144) + char2num[s[i]]
            if num in num_set:
                if num not in num_res:
                    num_res.append(num)
            else:
                num_set.add(num)
        return [self.num2str(res_num) for res_num in num_res]


def test(data_test):
    s = Solution()
    return s.findRepeatedDnaSequences(*data_test)


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
        ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"],
        ["AAAAAAAAAAAAA"],
        ["AAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTCCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTTAAAACCCCCAAAAACCCCCCAAAAAAAAACCCCCAAAAAAAAACCCCCAAAAACCCCCCAAAAAGGGTTTACCCCCCAAAAAGGGTTTAGGGTTTACCCCCCAAAAAGGGTTT"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
