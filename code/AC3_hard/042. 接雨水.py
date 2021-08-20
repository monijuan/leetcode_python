# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 14:39
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 042. 接雨水.py
# @Software: PyCharm
# ===================================
"""给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def oneSide2Highest(self,height: List[int]):
        res = 0
        highest = 0
        stack = []
        for now in height:
            if now<highest:
                stack.append(now)
            else:
                for h in stack:
                    res += min(now,highest)-h
                stack = [now]   # 注意，这个最高点之后还会用到
                highest = now
        return res,stack

    def trap(self, height: List[int]) -> int:
        """
        思路：
            （先假设最高的在最后边，如果在中间，对于右半部分而言就是向左的过程）
            从左往右爬格子，保存当前最高的格子 highest
            如果 now<highest 说明，now是可以存水的，但是可以存多少得看左右两边最高点中较低的那个减去now，把now入栈；
            如果 now>=highest 说明，在now左边的存多少水已经可以算出来了，不会更多了，所以逐个出栈，计算水量；
            到了最右了，如果栈中还有数，说明 HIGHEST 在中间，将栈中的数依次再来一遍，就相当于是从右往左找highest。
        :param height:
        :return:
        """
        res_left, stack = self.oneSide2Highest(height)   # 从左往右
        res_right, _ = self.oneSide2Highest(stack[::-1])  # 此时如果stack还有数，说明 highest 在中间，右边的数换个方向再来一遍
        return res_left + res_right


def test(data_test):
    s = Solution()
    return s.trap(*data_test)


if __name__ == '__main__':
    datas = [
        [[0,1,0,2,1,0,1,3,2,1,2,1]],#6
        [[4,2,0,3,2,5]],#9
        [[5,0,1]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
