# -*- coding: utf-8 -*-
# @Time    : 2022/4/24 16:15
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1898. 可移除字符的最大数目.py
# @Software: PyCharm 
# ===================================
"""给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组 removable ，该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。

请你找出一个整数 k（0 <= k <= removable.length），选出 removable 中的 前 k 个下标，然后从 s 中移除这些下标对应的 k 个字符。整数 k 需满足：在执行完上述步骤后， p 仍然是 s 的一个 子序列 。更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。

返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。

字符串的一个 子序列 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。

 

示例 1：

输入：s = "abcacb", p = "ab", removable = [3,1,0]
输出：2
解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
"ab" 是 "accb" 的一个子序列。
如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
因此，最大的 k 是 2 。
示例 2：

输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
输出：1
解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。
"abcd" 是 "abcddddd" 的一个子序列。
示例 3：

输入：s = "abcab", p = "abc", removable = [0,1,2,3,4]
输出：0
解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。
 

提示：

1 <= p.length <= s.length <= 105
0 <= removable.length < s.length
0 <= removable[i] < s.length
p 是 s 的一个 子字符串
s 和 p 都由小写英文字母组成
removable 中的元素 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-removable-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(m):
            removed = set(removable[:m])
            index, length = 0, len(s)
            for char in p:
                while index < length:
                    if index in removed:
                        index+=1
                        continue
                    elif s[index] != char:
                        index += 1
                    else:
                        break
                if index >= length:
                    return False
                index += 1
            return True

        l,r = 0,len(removable)
        while l<r:
            m = (l+r+1)>>1
            if check(m):
                l=m
            else:
                r=m-1
            # print(l,r,m)
        return l



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.maximumRemovals(*data)

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
        ["abcacb","ab",[3,1,0]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
