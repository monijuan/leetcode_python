# -*- coding: utf-8 -*-
# @Time    : 2022/1/30 10:20
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5994AC. 查找给定哈希值的子串.py
# @Software: PyCharm 
# ===================================
"""给定整数 p 和 m ，一个长度为 k 且下标从 0 开始的字符串 s 的哈希值按照如下函数计算：

hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.
其中 val(s[i]) 表示 s[i] 在字母表中的下标，从 val('a') = 1 到 val('z') = 26 。

给你一个字符串 s 和整数 power，modulo，k 和 hashValue 。请你返回 s 中 第一个 长度为 k 的 子串 sub ，满足 hash(sub, power, modulo) == hashValue 。

测试数据保证一定 存在 至少一个这样的子串。

子串 定义为一个字符串中连续非空字符组成的序列。



示例 1：

输入：s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
输出："ee"
解释："ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。
"ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。
示例 2：

输入：s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
输出："fbx"
解释："fbx" 的哈希值为 hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 312) mod 100 = 23132 mod 100 = 32 。
"bxz" 的哈希值为 hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 312) mod 100 = 25732 mod 100 = 32 。
"fbx" 是长度为 3 的第一个哈希值为 32 的子串，所以我们返回 "fbx" 。
注意，"bxz" 的哈希值也为 32 ，但是它在字符串中比 "fbx" 更晚出现。


提示：

1 <= k <= s.length <= 2 * 104
1 <= power, modulo <= 109
0 <= hashValue < modulo
s 只包含小写英文字母。
测试数据保证一定 存在 满足条件的子串。
"""
from leetcode_python.utils import *

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        l = len(s)
        orda = ord('a')
        nums = [ord(si)-orda+1 for si in s]
        powk_1 = pow(power,k-1,modulo)
        # print(nums,'powk_1:',powk_1)
        # ###
        # res = [0]*l
        # for i in range(l-1):
        #     res[i] = (nums[i]+nums[i+1]*pow(power,1,modulo))%modulo
        # print('res',res)
        # ###
        hash_id = [0]*l
        # hash s0
        hash_s0 = 0
        i_s = l-k
        for i in range(l-1,l-k-1,-1):
            hash_s0 += nums[i] * pow(power,i-i_s,modulo)
            hash_s0 %= modulo
        hash_id[l-k]=hash_s0
        # print('hash_s0',hash_s0)
        # hash_s0 = 0
        for i in range(l-k-1,-1,-1):
            hash_s0 -= (nums[i+k] * powk_1)
            if hash_s0<0:hash_s0+=modulo
            hash_s0 *= power
            hash_s0 += nums[i]
            hash_s0 %= modulo
            hash_id[i] = hash_s0
            # print(hash_id,s[i:i+k+1],hash_id[i+1],'-',nums[i+k]* powk_1%modulo,'+',nums[i])
        i = hash_id.index(hashValue)
        # print(hash_id)
        return s[i:i+k]

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.subStrHash(*data)


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
        ["leetcode",7,20,2,0],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')