# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 18:45
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : Offer_day28_38. 字符串的排列.py
# @Software: PyCharm 
# ===================================
"""输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 

限制：

1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        self.res_index = []

    def dfs(self,index_list:List[int],remain_index:List[int]):
        if len(index_list)==self.length:
            self.res_index.append(index_list)
        else:
            for id,index in enumerate(remain_index):
                next_list = index_list.copy()
                next_remain = remain_index.copy()
                next_list.append(index)
                next_remain.pop(id)
                self.dfs(next_list,next_remain)

    def permutation(self, s: str) -> List[str]:
        self.length = len(s)
        self.dfs([],[x for x in range(self.length)])
        res = set()
        for index_list in self.res_index:
            res.add(''.join([s[id] for id in index_list]))
        return list(res)


def test(data_test):
    s = Solution()
    return s.permutation(*data_test)


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
        ['abcd'],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')