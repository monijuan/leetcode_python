# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 13:36
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1491. 去掉最低工资和最高工资后的工资平均值.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。

请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

 

示例 1：

输入：salary = [4000,3000,1000,2000]
输出：2500.00000
解释：最低工资和最高工资分别是 1000 和 4000 。
去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500
示例 2：

输入：salary = [1000,2000,3000]
输出：2000.00000
解释：最低工资和最高工资分别是 1000 和 3000 。
去掉最低工资和最高工资以后的平均工资是 (2000)/1= 2000
示例 3：

输入：salary = [6000,5000,4000,3000,2000,1000]
输出：3500.00000
示例 4：

输入：salary = [8000,9000,2000,3000,6000,1000]
输出：4750.00000
 

提示：

3 <= salary.length <= 100
10^3 <= salary[i] <= 10^6
salary[i] 是唯一的。
与真实值误差在 10^-5 以内的结果都将视为正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)[1:-1]
        return sum(salary)/len(salary)


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
