# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 17:25
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 银联-03. 理财产品.py
# @Software: PyCharm 
# ===================================
"""某公司计划推出一批投资项目。 product[i] = price 表示第 i 个理财项目的投资金额 price 。客户在按需投资时，需要遵循以下规则：

客户在首次对项目 product[i] 投资时，需要投入金额 price
对已完成首次投资的项目 product[i] 可继续追加投入，但追加投入的金额需小于上一次对该项目的投入(追加投入为大于 0 的整数)
为控制市场稳定，每人交易次数不得大于 limit。(首次投资和追加投入均记作 1 次交易)
若对所有理财项目中最多进行 limit 次交易，使得投入金额总和最大，请返回这个最大值的总和。

注意：

答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1
示例 1：

输入：product = [4,5,3], limit = 8

输出：26

解释：满足条件的一种情况为：
第一个理财项目进行金额为 4，3，2 的交易；
第二个理财项目进行金额为 5，4，3 的交易；
第三个理财项目进行金额为 3，2 的交易；
得到最大投入金额总和为 5 + 4 * 2 + 3 * 3 + 2 * 2 = 26。

示例 2：

输入：product = [2,1,3], limit = 20

输出：10

解释：可交易总次数小于 limit，因此进行所有交易
第一个理财项目可交易 2 次，交易的金额分别为 2，1；
第二个理财项目可交易 1 次，交易的金额分别为 1；
第三个理财项目可交易 3 次，交易的金额分别为 3，2，1；
因此所得最大投入金额总和为 3 + 2 * 2 + 1 * 3 = 10。

提示：

1 <= product.length <= 10^5
1 <= product[i] <= 10^7
1 <= limit <= 10^9
"""
from leetcode_python.utils import *


class Solution:
    def maxInvestment(self, product: List[int], limit: int) -> int:


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

