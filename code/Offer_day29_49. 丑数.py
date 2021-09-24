# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 10:32
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day29_49. 丑数.py
# @Software: PyCharm
# ===================================
"""我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

# 错误c++代码
"""
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector<int> dp(n + 1);
        dp[1] = 1;
        int m = primes.size();
        vector<int> pointers(m, 1);
        for (int i = 2; i <= n; i++) {
            vector<int> nums(m);
            int minNum = INT_MAX;
            for (int j = 0; j < m; j++) {
                nums[j] = dp[pointers[j]] * primes[j];
                minNum = min(minNum, nums[j]);
            }
            dp[i] = minNum;
            for (int j = 0; j < m; j++) {
                if (minNum == nums[j]) {
                    pointers[j]++;
                }
            }
        }
        return dp[n];
    }
};
"""

class Solution:
    def __init__(self):
        pass

    def nthUglyNumber(self, n: int) -> int:
        return


def test(data_test):
    s = Solution()
    return s.nthUglyNumber(*data_test)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
