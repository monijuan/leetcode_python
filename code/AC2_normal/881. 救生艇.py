# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 9:15
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 881. 救生艇.py
# @Software: PyCharm
# ===================================
"""第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

 

示例 1：

输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
示例 2：

输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
示例 3：

输入：people = [3,5,3,4], limit = 5
输出：4
解释：4 艘船分别载 (3), (3), (4), (5)
提示：

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/boats-to-save-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class Solution:
    def __init__(self):
        """
        两个指针，[从小到大][从大到小]
        如果最大+最小>limit，最大的这个只能自己坐了
        """
        pass

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,j,times=0,len(people)-1,0
        people.sort()
        # 最大的要么自己上，要么带个最小的，如果能带个最小的就i+1
        while i<j:
            if people[i]+people[j]<=limit: i+=1
            j-=1
            times+=1
        # 如果最后还剩一个，也得算一次
        if i==j: times+=1
        return times


def test(data_test):
    s = Solution()
    return s.numRescueBoats(*data_test)


if __name__ == '__main__':
    datas = [
        [[1,2],3],      # 1
        [[3,2,2,1],3],  # 3
        [[3,5,3,4],5],  # 4
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
