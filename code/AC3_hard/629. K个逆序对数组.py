# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 9:04
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 629. K个逆序对数组.py
# @Software: PyCharm
# ===================================
"""给出两个整数 n 和 k，找出所有包含从 1 到 n 的数字，且恰好拥有 k 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第i个和第 j个元素，如果满i < j且 a[i] > a[j]，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 109 + 7 的值。

示例 1:

输入: n = 3, k = 0
输出: 1
解释:
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
示例 2:

输入: n = 3, k = 1
输出: 2
解释:
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
说明:

 n 的范围是 [1, 1000] 并且 k 的范围是 [0, 1000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-inverse-pairs-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        考虑最后一个数插在哪里？
            如果插在最后，逆序对的数目不会增加，就等于n-1的情况！
            如果插在x个数字的前面，逆序对的数目增加x，就是n-1的情况+x个逆序对！
            那么对于需要k个逆序对，就需要n-1的时候只有k-x个逆序对！
        可以得出计算公式：
            f(n,k) = f(n-1,k) + f(n-1,k-1) + .. + f(n-1,k-n+1)
        错位相减：
            f(n,k) = f(n,k-1) + f(n-1,k) - f(n-1,k-n)
        考虑边际条件：
            f(n,<0) = 0
            f(n,0) = 1 # 升序排列一种情况
            f(1,>0) = 0  # 只有一个数，不存在逆序对
        """
        pass

    @lru_cache(None)
    def kInversePairs(self, n: int, k: int) -> int:
        if k==0: return 1
        elif k<0 or n==1: return 0
        else:return (self.kInversePairs(n,k-1) + self.kInversePairs(n-1,k) - self.kInversePairs(n-1,k-n))%(10**9+7)

def test(data_test):
    s = Solution()
    return s.kInversePairs(*data_test)


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
        [1,2],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
