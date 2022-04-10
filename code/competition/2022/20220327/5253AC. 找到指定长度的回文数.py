# -*- coding: utf-8 -*-
# @Time    : 2022/3/27 10:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5253AC. 找到指定长度的回文数.py
# @Software: PyCharm 
# ===================================
"""给你一个整数数组 queries 和一个 正 整数 intLength ，请你返回一个数组 answer ，其中 answer[i] 是长度为 intLength 的 正回文数 中第 queries[i] 小的数字，如果不存在这样的回文数，则为 -1 。

回文数 指的是从前往后和从后往前读一模一样的数字。回文数不能有前导 0 。



示例 1：

输入：queries = [1,2,3,4,5,90], intLength = 3
输出：[101,111,121,131,141,999]
解释：
长度为 3 的最小回文数依次是：
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, ...
第 90 个长度为 3 的回文数是 999 。
示例 2：

输入：queries = [2,4,6], intLength = 4
输出：[1111,1331,1551]
解释：
长度为 4 的前 6 个回文数是：
1001, 1111, 1221, 1331, 1441 和 1551 。


提示：

1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15
"""
from leetcode_python.utils import *

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def do(idx):
            l = (intLength+1)//2
            s = str(10**(l-1)+idx-1)
            # print(idx,l,s,s[l-1:],s[l-1::-1])
            if intLength>1:
                s+=s[intLength//2-1::-1]
            # print(s)
            return int(s) if int(s)<10**intLength else -1
        res = [do(i) for i in queries]
        # print(res)
        return res



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.kthPalindrome(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        # [[1,2,3,4,5,90],3],
        # [[1,2,3,4,5,90],5],
        [[2,201429812,8,520498110,492711727,339882032,462074369,9,7,6],1],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
