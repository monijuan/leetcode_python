# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 9:30
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1058. 最小化舍入误差以满足目标.py
# @Software: PyCharm
# ===================================
"""给定一系列价格 [p1,p2...,pn] 和一个目标 target，将每个价格 pi 舍入为 Roundi(pi) 以使得舍入数组 [Round1(p1),Round2(p2)...,Roundn(pn)] 之和达到给定的目标值 target。每次舍入操作 Roundi(pi) 可以是向下舍 Floor(pi) 也可以是向上入 Ceil(pi)。

如果舍入数组之和无论如何都无法达到目标值 target，就返回字符串 "-1"。否则，以保留到小数点后三位的字符串格式返回最小的舍入误差，其定义为 Σ |Roundi(pi) - (pi)|（ i 从 1 到 n ）。

 

示例 1：

输入：prices = ["0.700","2.800","4.900"], target = 8
输出："1.000"
解释：
使用 Floor，Ceil 和 Ceil 操作得到 (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 。
示例 2：

输入：prices = ["1.500","2.500","3.500"], target = 10
输出："-1"
解释：
达到目标是不可能的。
示例 3：

输入：prices = ["1.500","2.500","3.500"], target = 9
输出："1.500"
 

提示：

1 <= prices.length <= 500
表示价格的每个字符串 prices[i] 都代表一个介于 [0.0, 1000.0] 之间的实数，并且正好有 3 个小数位。
target 介于 0 和 1000000 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimize-rounding-error-to-meet-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        left = right = 0
        decimal = []
        for p in prices:
            num = float(p)
            left+=math.floor(num)
            right+=math.ceil(num)
            decimal.append(num%1)
        if left<=target<=right:
            decimal.sort()
            num_ceil = target-left  # 有num_ceil 个需要向上取整
            res = sum(decimal[:-num_ceil]) + num_ceil-sum(decimal[-num_ceil:])
            return f'{abs(res):.03f}'
        else:
            return "-1"


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
