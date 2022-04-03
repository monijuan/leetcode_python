# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 9:07
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 字符串哈希.py
# @Software: PyCharm 
# ===================================
"""
6036. 构造字符串的总得分和
https://leetcode-cn.com/problems/sum-of-scores-of-built-strings/solution/ts-er-fen-zi-fu-chuan-ha-xi-by-981377660-u7i4/
"""

from typing import Sequence
class hash_字符串哈希:
    _BASE = 131
    _MOD = 2 ** 64
    _OFFSET = 96

    @staticmethod
    def setBASE(base: int) -> None:
        hash_字符串哈希._BASE = base

    @staticmethod
    def setMOD(mod: int) -> None:
        hash_字符串哈希._MOD = mod

    @staticmethod
    def setOFFSET(offset: int) -> None:
        hash_字符串哈希._OFFSET = offset

    def __init__(self, sequence: Sequence[str]):
        self._sequence = sequence
        self._prefix = [0] * (len(sequence) + 1)
        self._base = [0] * (len(sequence) + 1)
        self._prefix[0] = 0
        self._base[0] = 1
        for i in range(1, len(sequence) + 1):
            self._prefix[i] = (
                self._prefix[i - 1] * hash_字符串哈希._BASE + ord(sequence[i - 1]) - self._OFFSET
            ) % hash_字符串哈希._MOD
            self._base[i] = (self._base[i - 1] * hash_字符串哈希._BASE) % hash_字符串哈希._MOD

    def getHashOfSlice(self, left: int, right: int) -> int:
        """s[left:right]的哈希值"""
        assert 0 <= left <= right <= len(self._sequence)
        left += 1
        upper = self._prefix[right]
        lower = self._prefix[left - 1] * self._base[right - (left - 1)]
        return (upper - lower) % hash_字符串哈希._MOD



class Solution_6036_构造字符串的总得分和:
    def sumScores(self, s: str) -> int:
        def countPre(curLen: int, start: int) -> int:
            left, right = 1, curLen
            while left <= right:
                mid = (left + right) // 2
                if hasher.getHashOfSlice(start, start + mid) == hasher.getHashOfSlice(0, mid):
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        n = len(s)
        hash_字符串哈希.setMOD(151217133020331712151)
        hasher = hash_字符串哈希(s)

        res = 0
        for i in range(1, n + 1):
            if s[-i] != s[0]:
                continue
            count = countPre(i, n - i)
            res += count
        return res

if __name__ == '__main__':
    s = 'kljqhwbdoq'
    hash_字符串哈希.setMOD(151217133020331712151)
    hasher = hash_字符串哈希(s)
    l,r = 2,4
    print(s[2:4],hasher.getHashOfSlice(2,4))    # s[l:r]

