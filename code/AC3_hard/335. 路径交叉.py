# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 10:19
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 335. 路径交叉.py
# @Software: PyCharm
# ===================================
"""给你一个整数数组 distance 。

从 X-Y 平面上的点 (0,0) 开始，先向北移动 distance[0] 米，然后向西移动 distance[1] 米，向南移动 distance[2] 米，向东移动 distance[3] 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。

 

示例 1：


输入：distance = [2,1,1,2]
输出：true
示例 2：


输入：distance = [1,2,3,4]
输出：false
示例 3：


输入：distance = [1,1,1,1]
输出：true
 

提示：

1 <= distance.length <= 105
1 <= distance[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-crossing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def isSelfCrossing(self, distance: List[int]) -> bool:
        """参考了官方解答https://leetcode-cn.com/problems/self-crossing/solution/lu-jing-jiao-cha-by-leetcode-solution-dekx/"""
        n = len(distance)
        for i in range(3, n):
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]: return True
            if i == 4 and (distance[3] == distance[1] and distance[4] >= distance[2] - distance[0]): return True
            if i >= 5 and (distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3] and distance[i] >= distance[i - 2] - distance[i - 4] and distance[i - 2] > distance[i - 4]): return True
        return False



def test(data_test):
    s = Solution()
    return s.isSelfCrossing(*data_test)


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
