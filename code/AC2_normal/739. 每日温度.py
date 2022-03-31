# -*- coding: utf-8 -*-
# @Time    : 2022/3/31 9:18
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 739. 每日温度.py
# @Software: PyCharm 
# ===================================
"""给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i 天之后，才会有更高的温度。如果气温在这之后都不会升高，请在该位置用 0 来代替。

 

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]
 

提示：

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution_tle:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        l=len(temperatures)
        ma = max(temperatures)
        for i,x in enumerate(temperatures):
            if x==ma:
                res.append(0)
                continue
            j=i
            while j<l and temperatures[j]<=x:j+=1
            res.append(j-i if j<l else 0)
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, nxt = [0] * n, [n]*102
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt[t] for t in range(temperatures[i] + 1, 102))
            if warmer_index!=n:
                ans[i] = warmer_index - i
            nxt[temperatures[i]] = i
        return ans


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
