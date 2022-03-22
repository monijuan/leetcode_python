# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 10:29
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6016AC. Excel 表中某个范围内的单元格.py
# @Software: PyCharm 
# ===================================
"""Excel 表中的一个单元格 (r, c) 会以字符串 "<col><row>" 的形式进行表示，其中：

<col> 即单元格的列号 c 。用英文字母表中的 字母 标识。
例如，第 1 列用 'A' 表示，第 2 列用 'B' 表示，第 3 列用 'C' 表示，以此类推。
<row> 即单元格的行号 r 。第 r 行就用 整数 r 标识。
给你一个格式为 "<col1><row1>:<col2><row2>" 的字符串 s ，其中 <col1> 表示 c1 列，<row1> 表示 r1 行，<col2> 表示 c2 列，<row2> 表示 r2 行，并满足 r1 <= r2 且 c1 <= c2 。

找出所有满足 r1 <= x <= r2 且 c1 <= y <= c2 的单元格，并以列表形式返回。单元格应该按前面描述的格式用 字符串 表示，并以 非递减 顺序排列（先按列排，再按行排）。



示例 1：



输入：s = "K1:L2"
输出：["K1","K2","L1","L2"]
解释：
上图显示了列表中应该出现的单元格。
红色箭头指示单元格的出现顺序。
示例 2：



输入：s = "A1:F1"
输出：["A1","B1","C1","D1","E1","F1"]
解释：
上图显示了列表中应该出现的单元格。
红色箭头指示单元格的出现顺序。


提示：

s.length == 5
'A' <= s[0] <= s[3] <= 'Z'
'1' <= s[1] <= s[4] <= '9'
s 由大写英文字母、数字、和 ':' 组成
"""
from leetcode_python.utils import *


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1,r1,_,c2,r2 = list(s)
        # print(c1,r1,c2,r2)
        ranger = range(ord(c1),ord(c2)+1)
        ranger = [chr(c) for c in ranger]
        rangec = list(range(int(r1),int(r2)+1))
        # print(ranger,rangec)
        res = []
        for r in ranger:
            for c in rangec:
                res.append(f'{r}{c}')
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.cellsInRange(*data)


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
        ["A1:F1"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

