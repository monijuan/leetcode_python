# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 16:23
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 278. 第一个错误的版本.py
# @Software: PyCharm
# ===================================
"""你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

 
示例 1：

输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。
示例 2：

输入：n = 1, bad = 1
输出：1
 

提示：

1 <= bad <= n <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version)->bool:
    if version>=4:return True
    else:return False

class Solution:
    def __init__(self):
        pass

    def firstBadVersion(self, n: int)->int:
        if n==1:return 1
        ppp = (n+1)//2
        while not isBadVersion(ppp): ppp += (n-ppp+1)//2 # 二分查找不是错的
        if not isBadVersion(ppp-1):return ppp
        else: return self.firstBadVersion(ppp-1)


def test(data_test):
    s = Solution()
    return s.firstBadVersion(*data_test)


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
        [5],
        # [10],
        # [11],
        [100],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
