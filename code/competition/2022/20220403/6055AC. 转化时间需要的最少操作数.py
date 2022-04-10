# -*- coding: utf-8 -*-
# @Time    : 2022/4/3 10:28
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6055AC. 转化时间需要的最少操作数.py
# @Software: PyCharm 
# ===================================
"""给你两个字符串 current 和 correct ，表示两个 24 小时制时间 。

24 小时制时间 按 "HH:MM" 进行格式化，其中 HH 在 00 和 23 之间，而 MM 在 00 和 59 之间。最早的 24 小时制时间为 00:00 ，最晚的是 23:59 。

在一步操作中，你可以将 current 这个时间增加 1、5、15 或 60 分钟。你可以执行这一操作 任意 次数。

返回将 current 转化为 correct 需要的 最少操作数 。



示例 1：

输入：current = "02:30", correct = "04:35"
输出：3
解释：
可以按下述 3 步操作将 current 转换为 correct ：
- 为 current 加 60 分钟，current 变为 "03:30" 。
- 为 current 加 60 分钟，current 变为 "04:30" 。
- 为 current 加 5 分钟，current 变为 "04:35" 。
可以证明，无法用少于 3 步操作将 current 转化为 correct 。
示例 2：

输入：current = "11:00", correct = "11:01"
输出：1
解释：只需要为 current 加一分钟，所以最小操作数是 1 。


提示：

current 和 correct 都符合 "HH:MM" 格式
current <= correct
"""
from leetcode_python.utils import *


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        m1 = int(current[:2]) * 60 + int(current[3:5])
        m2 = int(correct[:2]) * 60 + int(correct[3:5])
        diss = m2 - m1
        res = diss // 60
        diss %= 60
        res += diss // 15
        diss %= 15
        res += diss // 5
        diss %= 5
        res += diss
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
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
