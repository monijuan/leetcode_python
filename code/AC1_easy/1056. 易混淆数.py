# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 10:11
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1056. 易混淆数.py
# @Software: PyCharm
# ===================================
"""给定一个数字 N，当它满足以下条件的时候返回 true：

原数字旋转 180° 以后可以得到新的数字。

如 0, 1, 6, 8, 9 旋转 180° 以后，得到了新的数字 0, 1, 9, 8, 6 。

2, 3, 4, 5, 7 旋转 180° 后，得到的不是数字。

易混淆数 (confusing number) 在旋转180°以后，可以得到和原来不同的数，且新数字的每一位都是有效的。

 

示例 1：



输入：6
输出：true
解释：
把 6 旋转 180° 以后得到 9，9 是有效数字且 9!=6 。
示例 2：



输入：89
输出：true
解释:
把 89 旋转 180° 以后得到 68，86 是有效数字且 86!=89 。
示例 3：



输入：11
输出：false
解释：
把 11 旋转 180° 以后得到 11，11 是有效数字但是值保持不变，所以 11 不是易混淆数字。
示例 4：



输入：25
输出：false
解释：
把 25 旋转 180° 以后得到的不是数字。
 

提示：

0 <= N <= 10^9
可以忽略掉旋转后得到的前导零，例如，如果我们旋转后得到 0008 那么该数字就是 8 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/confusing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def confusingNumber(self, n: int) -> bool:
        mp = [0, 1, 2, 3, 4, 5, 9, 7, 8, 6]
        num_old,num_new = n,0
        while n:
            right = n % 10
            if right in [2, 3, 4, 5, 7]: return False
            else: num_new = num_new * 10 + mp[right]
            n //= 10
        return num_new!=num_old


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
