# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 8:54
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1220. 统计元音字母序列的数目.py
# @Software: PyCharm
# ===================================
"""给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
每个元音 'a' 后面都只能跟着 'e'
每个元音 'e' 后面只能跟着 'a' 或者是 'i'
每个元音 'i' 后面 不能 再跟着另一个 'i'
每个元音 'o' 后面只能跟着 'i' 或者是 'u'
每个元音 'u' 后面只能跟着 'a'
由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果。

 

示例 1：

输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。
示例 2：

输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。
示例 3：

输入：n = 5
输出：68
 

提示：

1 <= n <= 2 * 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-vowels-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

MOD = 10**9+7
class Solution:
    @lru_cache(None)
    def dfs(self,c,n):
        if 0==n:return 1
        if c=='a':
            return self.dfs('e',n-1) % MOD
        elif c=='e':
            return (self.dfs('a',n-1)+self.dfs('i',n-1))%MOD
        elif c=='i':
            return (self.dfs('a',n-1)+self.dfs('e',n-1)+self.dfs('o',n-1)+self.dfs('u',n-1))%MOD
        elif c=='o':
            return (self.dfs('i',n-1)+self.dfs('u',n-1))%MOD
        else:
            return self.dfs('a',n-1)%MOD

    def countVowelPermutation(self, n: int) -> int:
        return (self.dfs('a',n-1) + self.dfs('e',n-1) + self.dfs('i',n-1) + self.dfs('o',n-1)+self.dfs('u',n-1))%MOD


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.countVowelPermutation(*data)


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
        [5],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
