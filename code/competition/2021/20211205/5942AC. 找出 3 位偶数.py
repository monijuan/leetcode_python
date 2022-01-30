# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 10:00
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5942AC. 找出 3 位偶数.py
# @Software: PyCharm 
# ===================================
"""
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
给你一个整数数组 digits ，其中每个元素是一个数字（0 - 9）。数组中可能存在重复元素。

你需要找出 所有 满足下述条件且 互不相同 的整数：

该整数由 digits 中的三个元素按 任意 顺序 依次连接 组成。
该整数不含 前导零
该整数是一个 偶数
例如，给定的 digits 是 [1, 2, 3] ，整数 132 和 312 满足上面列出的全部条件。

将找出的所有互不相同的整数按 递增顺序 排列，并以数组形式返回。



示例 1：

输入：digits = [2,1,3,0]
输出：[102,120,130,132,210,230,302,310,312,320]
解释：
所有满足题目条件的整数都在输出数组中列出。
注意，答案数组中不含有 奇数 或带 前导零 的整数。
示例 2：

输入：digits = [2,2,8,8,2]
输出：[222,228,282,288,822,828,882]
解释：
同样的数字（0 - 9）在构造整数时可以重复多次，重复次数最多与其在 digits 中出现的次数一样。
在这个例子中，数字 8 在构造 288、828 和 882 时都重复了两次。
示例 3：

输入：digits = [3,7,5]
输出：[]
解释：
使用给定的 digits 无法构造偶数。
示例 4：

输入：digits = [0,2,0,0]
输出：[200]
解释：
唯一一个不含 前导零 且满足全部条件的整数是 200 。
示例 5：

输入：digits = [0,0,0]
输出：[]
解释：
构造的所有整数都会有 前导零 。因此，不存在满足题目条件的整数。


提示：

3 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for i,num1 in enumerate(digits):
            if num1==0:continue
            for j,num2 in enumerate(digits):
                if i==j:continue
                for k,num3 in enumerate(digits):
                    if k in [i,j] or num3&1:continue
                    res.add(num1*100+num2*10+num3)
        return sorted(list(res))


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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