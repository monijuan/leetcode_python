# -*- coding: utf-8 -*-
# @Time    : 2021/12/12 10:27
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 5954AC. 给植物浇水 II.py
# @Software: PyCharm 
# ===================================
"""Alice 和 Bob 打算给花园里的 n 株植物浇水。植物排成一行，从左到右进行标记，编号从 0 到 n - 1 。其中，第 i 株植物的位置是 x = i 。

每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐，最初是满的 。他们按下面描述的方式完成浇水：

 Alice 按 从左到右 的顺序给植物浇水，从植物 0 开始。Bob 按 从右到左 的顺序给植物浇水，从植物 n - 1 开始。他们 同时 给植物浇水。
如果没有足够的水 完全 浇灌下一株植物，他 / 她会立即重新灌满浇水罐。
不管植物需要多少水，浇水所耗费的时间都是一样的。
不能 提前重新灌满水罐。
每株植物都可以由 Alice 或者 Bob 来浇水。
如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。
给你一个下标从 0 开始的整数数组 plants ，数组由 n 个整数组成。其中，plants[i] 为第 i 株植物需要的水量。另有两个整数 capacityA 和 capacityB 分别表示 Alice 和 Bob 水罐的容量。返回两人浇灌所有植物过程中重新灌满水罐的 次数 。



示例 1：

输入：plants = [2,2,3,3], capacityA = 5, capacityB = 5
输出：1
解释：
- 最初，Alice 和 Bob 的水罐中各有 5 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在分别剩下 3 单元和 2 单元水。
- Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 2 ，所以他先重新装满水，再浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 0 = 1 。
示例 2：

输入：plants = [2,2,3,3], capacityA = 3, capacityB = 4
输出：2
解释：
- 最初，Alice 的水罐中有 3 单元水，Bob 的水罐中有 4 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在都只有 1 单元水，并分别需要给植物 1 和植物 2 浇水。
- 由于他们的水量均不足以浇水，所以他们重新灌满水罐再进行浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 1 + 1 + 0 = 2 。
示例 3：

输入：plants = [5], capacityA = 10, capacityB = 8
输出：0
解释：
- 只有一株植物
- Alice 的水罐有 10 单元水，Bob 的水罐有 8 单元水。因此 Alice 的水罐中水更多，她会给这株植物浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 。
示例 4：

输入：plants = [1,2,4,4,5], capacityA = 6, capacityB = 5
输出：2
解释：
- 最初，Alice 的水罐中有 6 单元水，Bob 的水罐中有 5 单元水。
- Alice 给植物 0 浇水，Bob 给植物 4 浇水。
- Alice 和 Bob 现在分别剩下 5 单元和 0 单元水。
- Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 3 ，所以他先重新装满水，再浇水。
- Alice 和 Bob 现在分别剩下 3 单元和 1 单元水。
- 由于 Alice 的水更多，所以由她给植物 2 浇水。然而，她水罐里的水不够给植物 2 ，所以她先重新装满水，再浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 1 + 0 = 2 。
示例 5：

输入：plants = [2,2,5,2,2], capacityA = 5, capacityB = 5
输出：1
解释：
Alice 和 Bob 都会到达中间的植物，并且此时他俩剩下的水量相同，所以 Alice 会给这株植物浇水。
由于她到达时只剩下 1 单元水，所以需要重新灌满水罐。
这是唯一一次需要重新灌满水罐的情况。所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 1 。


提示：

n == plants.length
1 <= n <= 105
1 <= plants[i] <= 106
max(plants[i]) <= capacityA, capacityB <= 109
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        self.fruits = fruits
        self.startPos = startPos
        self.k=k
        res = 0
        # 先往左再拐到右边
        sum_now = 0
        pos_li = []
        for pos,num in fruits:
            if startPos - pos>k:continue
            elif pos-k>startPos:break
            sum_now+=num
            if startPos>pos:
                pos_li.append((pos,num))
            elif pos>startPos:
                while len(pos_li) and pos+startPos-2*pos_li[0][0]>k:
                    lllleft,llllnum = pos_li.pop(0)
                    sum_now-=llllnum
            res = max(res, sum_now)
        pos_li= []
        sum_now = 0
        for pos,num in fruits[::-1]:
            if pos-startPos>k:continue
            elif pos<startPos-k:break
            sum_now+=num
            if pos>startPos:
                pos_li.append((pos,num))
            elif pos<startPos:
                while len(pos_li) and 2*pos_li[0][0]-startPos-pos>k:
                    rrrright,rrrrnum = pos_li.pop(0)
                    sum_now-=rrrrnum
            res = max(res, sum_now)
        return res


    @lru_cache(None)
    def getsum_left(self,left):
        return sum([num for pos,num in self.fruits if left<=pos<=max(self.startPos,self.k+left+left-self.startPos)])

    @lru_cache(None)
    def getsum_right(self,right):
        return sum([num for pos,num in self.fruits if min(self.startPos,right+right-self.startPos - self.k)<=pos<=right])

    def maxTotalFruits_超时(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        self.fruits = fruits
        self.startPos = startPos
        self.k=k
        res = 0
        # 先往左再拐到右边
        for pos,num in fruits:
            if startPos - pos>k:continue
            elif pos - startPos>k:break
            if startPos>=pos:
                res = max(res,self.getsum_left(pos))
            if pos>=startPos:
                res = max(res,self.getsum_right(pos))
            print(pos,res)
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.maxTotalFruits(*data)


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
        # [[[2,8],[6,3],[8,6]],5,4],
        # [[[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]],5,4],
        [[[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]],21,30],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')