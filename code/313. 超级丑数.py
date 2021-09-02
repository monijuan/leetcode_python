# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 14:39
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 313. 超级丑数.py
# @Software: PyCharm
# ===================================
"""
"""
from typing import List

import numpy as np
class Solution:
    def __init__(self):
        self.prime_in_set=None
        self.is_prime=set([2])
        self.is_super_ugly_number=set([1])    # 加速
        self.now_max_prime=1

        self.ISDEBUG=False

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [None for _ in range(n+1)]     # 丑数序列
        res = 1                            # 第一个是1
        len_primes = len(primes)
        nums = [None for _ in range(len_primes)]
        pointers = [1 for _ in range(len_primes)]   # 指向该做乘积的那个丑数
        for i in range(2,n+1):
            min_newUgly = sys.maxsize
            for j in range(len_primes):
                nums[j] = dp[pointers[j]]*primes[j]
                min_newUgly = min(min_newUgly,nums[j])
            dp[i] = min_newUgly
            for j in range(len_primes):
                if min_newUgly==nums[j]:
                    pointers[j]+=1
        return dp[n]

    # 动态规划_超时
    def nthSuperUglyNumber_动态规划_超时(self, n: int, primes: List[int]) -> int:
        dp = [None for _ in range(n+1)]     # 丑数序列
        dp[1] = 1                             # 第一个是1
        len_primes = len(primes)
        nums = [None for _ in range(len_primes)]
        pointers = [1 for _ in range(len_primes)]   # 指向该做乘积的那个丑数
        for i in range(2,n+1):
            min_newUgly = sys.maxsize
            for j in range(len_primes):
                nums[j] = dp[pointers[j]]*primes[j]
                min_newUgly = min(min_newUgly,nums[j])
            dp[i] = min_newUgly
            for j in range(len_primes):
                if min_newUgly==nums[j]:
                    pointers[j]+=1
        return dp[n]


    # 暴力判断超级丑数
    def deepDivision(self,father,divisor):
        """返回 father不断除以divisor 直到不能整除"""
        while father%divisor==0:
            father/=divisor
        return father

    def isPrime(self,number):
        """判断输入是否为素数"""
        if number in self.is_prime:return True
        if number<2:return False
        for x in range(2, int(np.sqrt(number)) + 1):
            if number%x==0:return False
        return True

    def isSuperUglyNumber(self,number):
        """判断 number 是否为超级丑数 """
        number_division=number
        # 如果质因数都在现有 is_prime 里，只要分析是否都在 prime_in_set 中即可
        for prime in self.is_prime:
            if number_division%prime==0:
                if prime in self.prime_in_set:
                    number_division=self.deepDivision(number_division,prime)
                else: return False
        if number_division==1:
            # self.is_super_ugly_number.add(number)
            return True

        # 如果因数全是超级丑数，那么他肯定也是超级丑数
        for primeinset in self.prime_in_set:
            if 1!=primeinset and number_division%primeinset==0:
                number_division=self.deepDivision(number_division,primeinset)
            # if primeinset>number_division:break
        if number_division==1:
            # self.is_super_ugly_number.add(number)
            return True

        # 已经是质数了
        if self.isPrime(number_division): return number_division in self.prime_in_set

        # 有更大的质因数
        num = max(self.is_prime)
        while num<number_division:
            num+=1
            if number_division%num==0 and self.isPrime(num):
                self.is_prime.add(num)
                if num not in self.prime_in_set:
                    return False
                number_division = self.deepDivision(number_division,num)
        # self.is_super_ugly_number.add(number)
        return True

    def nthSuperUglyNumber_暴力超时(self, n: int, primes: List[int]) -> int:
        self.prime_in_set = primes
        result = 1
        cnt = 1 # 第一个永远是1，所以至少有一个
        number = 1  # 从2开始分析
        while cnt<n:
            number += 1
            if self.isSuperUglyNumber(number):
                result = number
                cnt+=1
        return result


import sys
def test(n=12,primes=[2,7,13,19]):
    s = Solution()
    return s.nthSuperUglyNumber(n,primes)
    # return s.nthSuperUglyNumber2(n,primes)

if __name__ == '__main__':
    import time
    data_test = [
        # [12,[2,7,13,19]],   # [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
        # [500,[37, 43, 59, 61, 67, 71, 79, 83, 89, 97, 101, 103, 113, 127, 131, 157, 163, 167, 173, 179, 191, 193, 197, 199, 211, 229, 233, 239, 251, 257]],
        # [800,[37, 43, 59, 61, 67, 71, 79, 83, 89, 97, 101, 103, 113, 127, 131, 157, 163, 167, 173, 179, 191, 193, 197, 199, 211, 229, 233, 239, 251, 257]],
        # [3000,[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]],
        # [3000,[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]],
        # [3000,[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]],
        # [100000,[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]],
        [1000000,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]],
    ]
    for n,p in data_test:
        t0 = time.time()
        print('result:',test(n,p),f'{time.time()-t0}s')
