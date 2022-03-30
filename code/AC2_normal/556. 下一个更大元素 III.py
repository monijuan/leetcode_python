# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 21:17
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 556. 下一个更大元素 III.py
# @Software: PyCharm 
# ===================================
"""给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

 

示例 1：

输入：n = 12
输出：21
示例 2：

输入：n = 21
输出：-1
 

提示：

1 <= n <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import bisect

from leetcode_python.utils import *

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        chars = [int(x) for x in list(str(n)[::-1])]
        i,last,l = 0,-1,len(chars)
        while i<l and chars[i]>=last:
            last = chars[i]
            i+=1
        if i>=l:return -1
        sortnums = sorted(chars[:i+1])
        idx = bisect.bisect_right(sortnums,chars[i])
        hd = sortnums[idx]
        sortnums.remove(hd)
        res = int(''.join([str(x) for x in sorted(sortnums)[::-1]+[hd]+chars[i+1::]])[::-1])
        return -1 if res>2**31-1 else res

def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.nextGreaterElement(*data)

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
        [12354321],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
