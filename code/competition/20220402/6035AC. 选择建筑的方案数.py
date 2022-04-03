# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 8:53
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6035AC. 选择建筑的方案数.py
# @Software: PyCharm 
# ===================================
"""给你一个下标从 0 开始的二进制字符串 s ，它表示一条街沿途的建筑类型，其中：

s[i] = '0' 表示第 i 栋建筑是一栋办公楼，
s[i] = '1' 表示第 i 栋建筑是一间餐厅。
作为市政厅的官员，你需要随机 选择 3 栋建筑。然而，为了确保多样性，选出来的 3 栋建筑 相邻 的两栋不能是同一类型。

比方说，给你 s = "001101" ，我们不能选择第 1 ，3 和 5 栋建筑，因为得到的子序列是 "011" ，有相邻两栋建筑是同一类型，所以 不合 题意。
请你返回可以选择 3 栋建筑的 有效方案数 。

 

示例 1：

输入：s = "001101"
输出：6
解释：
以下下标集合是合法的：
- [0,2,4] ，从 "001101" 得到 "010"
- [0,3,4] ，从 "001101" 得到 "010"
- [1,2,4] ，从 "001101" 得到 "010"
- [1,3,4] ，从 "001101" 得到 "010"
- [2,4,5] ，从 "001101" 得到 "101"
- [3,4,5] ，从 "001101" 得到 "101"
没有别的合法选择，所以总共有 6 种方法。
示例 2：

输入：s = "11100"
输出：0
解释：没有任何符合题意的选择。
 

提示：

3 <= s.length <= 105
s[i] 要么是 '0' ，要么是 '1' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-to-select-buildings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def numberOfWays(self, s: str) -> int:
        def f(t):
            a = b = c = 0
            for x in s:
                if x==t[2]:c+=b
                if x==t[1]:b+=a
                if x==t[0]:a+=1
            return c
        return f('101')+f('010')


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
