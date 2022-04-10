# -*- coding: utf-8 -*-
# @Time    : 2022/3/20 10:16
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6028AC. 统计道路上的碰撞次数.py
# @Software: PyCharm 
# ===================================
"""在一条无限长的公路上有 n 辆汽车正在行驶。汽车按从左到右的顺序按从 0 到 n - 1 编号，每辆车都在一个 独特的 位置。

给你一个下标从 0 开始的字符串 directions ，长度为 n 。directions[i] 可以是 'L'、'R' 或 'S' 分别表示第 i 辆车是向 左 、向 右 或者 停留 在当前位置。每辆车移动时 速度相同 。

碰撞次数可以按下述方式计算：

当两辆移动方向 相反 的车相撞时，碰撞次数加 2 。
当一辆移动的车和一辆静止的车相撞时，碰撞次数加 1 。
碰撞发生后，涉及的车辆将无法继续移动并停留在碰撞位置。除此之外，汽车不能改变它们的状态或移动方向。

返回在这条道路上发生的 碰撞总次数 。



示例 1：

输入：directions = "RLRSLL"
输出：5
解释：
将会在道路上发生的碰撞列出如下：
- 车 0 和车 1 会互相碰撞。由于它们按相反方向移动，碰撞数量变为 0 + 2 = 2 。
- 车 2 和车 3 会互相碰撞。由于 3 是静止的，碰撞数量变为 2 + 1 = 3 。
- 车 3 和车 4 会互相碰撞。由于 3 是静止的，碰撞数量变为 3 + 1 = 4 。
- 车 4 和车 5 会互相碰撞。在车 4 和车 3 碰撞之后，车 4 会待在碰撞位置，接着和车 5 碰撞。碰撞数量变为 4 + 1 = 5 。
因此，将会在道路上发生的碰撞总次数是 5 。
示例 2：

输入：directions = "LLRR"
输出：0
解释：
不存在会发生碰撞的车辆。因此，将会在道路上发生的碰撞总次数是 0 。


提示：

1 <= directions.length <= 105
directions[i] 的值为 'L'、'R' 或 'S'
"""
from leetcode_python.utils import *

class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L')
        directions = directions.rstrip('R')
        return len(directions) - directions.count('S')

    def countCollisions_AC(self, directions: str) -> int:
        l = len(directions)
        flag = [0]*l

        i = 0
        beginrid,last = 0,'L'
        while i<l:
            now = directions[i]
            if last == 'R':
                if now == 'L':
                    flag[beginrid:i+1]=[1]*(i-beginrid+1)
                elif now == 'S':
                    flag[beginrid:i]=[1]*(i-beginrid)
            else:
                if now=='R':
                    beginrid=i
            last = now
            i+=1
        print(flag)

        change = ''
        for c in directions[::-1]:
            if c=='L':change+='R'
            elif c=='R':change+='L'
            else:change+='S'
        print(change)
        flag2 = [0]*l
        i = 0
        beginrid,last = 0,'L'
        while i<l:
            now = change[i]
            if last == 'R':
                if now in 'L':
                    flag2[beginrid:i+1]=[1]*(i-beginrid+1)
                elif now == 'S':
                    flag2[beginrid:i]=[1]*(i-beginrid)
            else:
                if now=='R':
                    beginrid=i
            last = now
            i+=1
        # print(flag2)
        resf = [a|b for a,b in zip(flag,flag2[::-1])]
        # print(resf)
        return sum(resf)


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countCollisions(*data)


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
        ["LLRR"],
        # ["RLRSLL"],
        # ["LLRLRLLSLRLLSLSSSS"],
        # ["RS"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

