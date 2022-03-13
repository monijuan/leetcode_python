# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 17:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 银联-04. 合作开发.py
# @Software: PyCharm 
# ===================================
"""为了不断提高用户使用的体验，开发团队正在对产品进行全方位的开发和优化。
已知开发团队共有若干名成员，skills[i] 表示第 i 名开发人员掌握技能列表。如果两名成员各自拥有至少一门对方未拥有的技能，则这两名成员可以「合作开发」。
请返回当前有多少对开发成员满足「合作开发」的条件。由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。

注意：

对于任意 skills[i] 均升序排列。
示例 1：

输入：
skills = [[1,2,3],[3],[2,4]]

输出: 2

解释：
开发成员 [1,2,3] 和成员 [2,4] 满足「合作开发」的条件，技能 1 和 4 分别是对方未拥有的技术
开发成员 [3] 和成员 [2,4] 满足「合作开发」的条件，技能 3 和 4 分别是对方未拥有的技术
开发成员 [1,2,3] 和成员 [3] 不满足「合作开发」的条件，由于开发成员 [3] 没有对方未拥有的技术
因此有 2 对开发成员满足「合作开发」的条件。

示例 2：

输入：
skills = [[3],[6]]

输出: 1

解释：
开发成员 [3] 和成员 [6] 满足「合作开发」的条件
因此有 1 对开发成员满足「合作开发」的条件。

提示：

2 <= skills.length <= 10^5
1 <= skills[i].length <= 4
1 <= skills[i][j] <= 1000
skills[i] 中不包含重复元素
"""
from leetcode_python.utils import *


class Solution:
    def coopDevelop(self, skills: List[List[int]]) -> int:


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

