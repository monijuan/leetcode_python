# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 15:59
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 面试题 05.02. 二进制数转字符串.py
# @Software: PyCharm
# ===================================
"""二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印“ERROR”。

示例1:

 输入：0.625
 输出："0.101"
示例2:

 输入：0.1
 输出："ERROR"
 提示：0.1无法被二进制准确表示
 

提示：

32位包括输出中的 "0." 这两位。
题目保证输入用例的小数位数最多只有 6 位

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/bianry-number-to-string-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def printBin(self, num: float) -> str:
        res = '0.'
        while num and len(res)<32:
            num*=2
            x = int(num)
            res+=str(x)
            num-=x
        return 'ERROR' if num else res



def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.printBin(*data)


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
        [0.625],
        [0.1],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
