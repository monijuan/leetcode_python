# -*- coding: utf-8 -*-
# @Time    : 2021/12/25 22:02
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5949AC. 一个区间内所有数乘积的缩写.py
# @Software: PyCharm 
# ===================================
"""给你两个正整数 left 和 right ，满足 left <= right 。请你计算 闭区间 [left, right] 中所有整数的 乘积 。

由于乘积可能非常大，你需要将它按照以下步骤 缩写 ：

统计乘积中 后缀 0 的数目，将这个数目记为 C 。
比方说，1000 中有 3 个后缀 0 ，546 中没有后缀 0 。
将乘积中剩余数字记为 d 。如果 d > 10 ，那么将乘积表示为 <pre>...<suf> 的形式，其中 <pre> 表示乘积最 开始 的 5 个数位，<suf> 表示删除后缀 0 之后 结尾的 5 个数位。如果 d <= 10 ，我们不对它做修改。
比方说，我们将 1234567654321 表示为 12345...54321 ，但是 1234567 仍然表示为 1234567 。
最后，将乘积表示为 字符串 "<pre>...<suf>eC" 。
比方说，12345678987600000 被表示为 "12345...89876e5" 。
请你返回一个字符串，表示 闭区间 [left, right] 中所有整数 乘积 的 缩写 。



示例 1：

输入：left = 1, right = 4
输出："24e0"
解释：
乘积为 1 × 2 × 3 × 4 = 24 。
由于没有后缀 0 ，所以 24 保持不变，缩写的结尾为 "e0" 。
因为乘积的结果是 2 位数，小于 10 ，所欲我们不进一步将它缩写。
所以，最终将乘积表示为 "24e0" 。
示例 2：

输入：left = 2, right = 11
输出："399168e2"
解释：
乘积为 39916800 。
有 2 个后缀 0 ，删除后得到 399168 。缩写的结尾为 "e2" 。
删除后缀 0 后是 6 位数，不需要进一步缩写。
所以，最终将乘积表示为 "399168e2" 。
示例 3：



输入：left = 999998, right = 1000000
输出："99999...00002e6"
解释：
上图展示了如何得到乘积的缩写 "99999...00002e6" 。
- 总共有 6 个后缀 0 。缩写的结尾为 "e6" 。
- 开头 5 个数位是 99999 。
- 删除后缀 0 后结尾 5 个数字为 00002 。
示例 4：

输入：left = 256, right = 65535
输出："23510...78528e16317"
解释：
乘积是一个非常大的数字：
- 总共有 16317 个后缀 0 。缩写结尾为 "e16317" 。
- 开头 5 个数字为 23510 。
- 删除后缀 0 后，结尾 5 个数字为 78528 。
所以，乘积的缩写为 "23510...78528e16317" 。


提示：

1 <= left <= right <= 106
"""
from leetcode_python.utils import *


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        n_0 = 0
        p = 1
        for x in range(right,left-1,-1):
            p*=x
            while 0==p%10:
                n_0+=1
                p//=10
            if len(str(p))>10:break
        else:return str(p)+f'e{n_0}'

        # 需要用...表示
        head,end,n_0 = 1,1,0
        for x in range(left,right+1):
            head*=x
            end*=x
            while head>1000000000000:head//=10
            while 0==end%10:
                n_0+=1
                end//=10
            end%=1000000000000
        while head > 100000: head //= 10
        end%=100000
        res = f'{head}...{end:05d}e{n_0}'
        return res

def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.abbreviateProduct(*data)


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
        # [2,11],
        [999998,1000000],   # 99999...00002e6
        [256,65535],    # 23510...78528e16317
        [18,75],    # 69749...47744e15
        [410,70833],    # "81384...08512e17604"
        [80952,506382], # "47396...47744e106358"
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')