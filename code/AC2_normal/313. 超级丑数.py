# -*- coding: utf-8 -*-
# @Time    : 2021/8/12 14:39
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 313. 超级丑数.py
# @Software: PyCharm
# ===================================
"""超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

 

示例 1：

输入：n = 12, primes = [2,7,13,19]
输出：32
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
示例 2：

输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
 
提示：

1 <= n <= 106
1 <= primes.length <= 100
2 <= primes[i] <= 1000
题目数据 保证 primes[i] 是一个质数
primes 中的所有值都 互不相同 ，且按 递增顺序 排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import numpy as np
import heapq


class Solution_ac__:
    def nthSuperUglyNumber_超时(self, n: int, primes: List[int]) -> int:
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

class Solution:
    def __init__(self):
        pass

    def nthSuperUglyNumber_ac(self, n: int, primes: List[int]) -> int:
        q = [(a, i, 0) for i, a in enumerate(primes)]
        ans = [1, ] + [0, ] * (n - 1)
        j = 1
        while j < n:
            val, i, idx = q[0]
            if val != ans[j - 1]:
                ans[j] = val
                j += 1
            heapq.heapreplace(q, (ans[idx + 1] * primes[i], i, idx + 1))
        return ans[n - 1]


    def nthSuperUglyNumber_动态规划2_超时(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        m = len(primes)
        pointers = [1] * m
        for i in range(2, n + 1):
            min_num = min(dp[pointers[j]] * primes[j] for j in range(m))
            dp[i] = min_num
            for j in range(m):
                if dp[pointers[j]] * primes[j] == min_num:
                    pointers[j] += 1
        return dp[n]

    def nthSuperUglyNumber_小顶堆超时(self, n: int, primes: List[int]) -> int:
        seen = {1}
        heap = [1]
        for i in range(n):
            ugly = heapq.heappop(heap)
            for prime in primes:
                nxt = ugly * prime
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return ugly


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



class Solution_暴力超时:
    def __init__(self):
        self.prime_in_set=None
        self.prime_not_in_set=[]
        self.is_prime=[2]
        self.is_super_ugly_number=[1,]    # 加速
        self.now_max_prime=1

        self.ISDEBUG=False

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
        # # 如果因数全是超级丑数，那么他肯定也是超级丑数
        # for super_ugly in self.is_super_ugly_number:
        #     if 1!=super_ugly and number_division%super_ugly==0:
        #         number_division=self.deepDivision(number_division,super_ugly)

        # 如果质因数都在现有 is_prime 里，只要分析是否都在 prime_in_set 中即可
        for prime in self.is_prime:
            if number_division%prime==0:
                if prime in self.prime_in_set:
                    number_division=self.deepDivision(number_division,prime)
                else:
                    return False
        if number_division==1:
            self.is_super_ugly_number.append(number)
            if self.ISDEBUG:print(f'add {number}, now {self.is_super_ugly_number}')
            return True

        # # 如果因数全是超级丑数，那么他肯定也是超级丑数
        # for primeinset in self.prime_in_set:
        #     if 1!=primeinset and number_division%primeinset==0:
        #         number_division=self.deepDivision(number_division,primeinset)
        # if number_division==1:
        #     self.is_super_ugly_number.append(number)
        #     if self.ISDEBUG:print(f'add {number}, now {self.is_super_ugly_number}')
        #     return True

        # number_division!=1 表示还有质因数不在 is_prime 中，可能有更大的质因数，也可能已经是质数了
        # 已经是质数了
        if self.isPrime(number_division):
            # self.is_prime.append(number_division)
            if number_division in self.prime_in_set:return True
            else:return False
        # 有更大的质因数
        num = max(self.is_prime)
        while num<number_division:
            num+=1
            if number_division%num==0 and self.isPrime(num):
                self.is_prime.append(num)
                if num not in self.prime_in_set:
                    return False
                number_division = self.deepDivision(number_division,num)
        else:
            self.is_super_ugly_number.append(number)
            if self.ISDEBUG:print(f'add {number}, now {self.is_super_ugly_number}')
            return True

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
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
        [3000,[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]],
        [100000,[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]],
        [1000000,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541]],
    ]
    for n,p in data_test:
        t0 = time.time()
        print('result:',test(n,p),f'{time.time()-t0}s')
