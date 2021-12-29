# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 9:11
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 47. 入场安检.py
# @Software: PyCharm
# ===================================
"""「力扣挑战赛」 的入场仪式马上就要开始了，由于安保工作的需要，设置了可容纳人数总和为 M 的 N 个安检室，capacities[i] 记录第 i 个安检室可容纳人数。安检室拥有两种类型：

先进先出：在安检室中的所有观众中，最早进入安检室的观众最先离开
后进先出：在安检室中的所有观众中，最晚进入安检室的观众最先离开


恰好 M+1 位入场的观众（编号从 0 开始）需要排队依次入场安检， 入场安检的规则如下：

观众需要先进入编号 0 的安检室
当观众将进入编号 i 的安检室时（0 <= i < N)，
若安检室未到达可容纳人数上限，该观众可直接进入；
若安检室已到达可容纳人数上限，在该观众进入安检室之前需根据当前安检室类型选择一位观众离开后才能进入；
当观众离开编号 i 的安检室时 （0 <= i < N-1)，将进入编号 i+1 的安检室接受安检。
若可以任意设定每个安检室的类型，请问有多少种设定安检室类型的方案可以使得编号 k 的观众第一个通过最后一个安检室入场。

注意：

观众不可主动离开安检室，只有当安检室容纳人数达到上限，且又有新观众需要进入时，才可根据安检室的类型选择一位观众离开；
由于方案数可能过大，请将答案对 1000000007 取模后返回。
示例 1：

输入：capacities = [2,2,3], k = 2

输出：2
解释：
存在两种设定的 2 种方案：

方案 1：将编号为 0 、1 的实验室设置为 后进先出 的类型，编号为 2 的实验室设置为 先进先出 的类型；
方案 2：将编号为 0 、1 的实验室设置为 先进先出 的类型，编号为 2 的实验室设置为 后进先出 的类型。
以下是方案 1 的示意图：


示例 2：

输入：capacities = [3,3], k = 3

输出：0

示例 3：

输入：capacities = [4,3,2,2], k = 6

输出：2

提示:

1 <= capacities.length <= 200
1 <= capacities[i] <= 200
0 <= k <= sum(capacities)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/oPs9Bm
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if k==0:return 1
        cnt = Counter()
        for num in nums:
            cnt_new = Counter([num])
            for s,c in cnt.items():
                if s+num>k:continue
                cnt_new[s+num]=c
            cnt+=cnt_new
        return cnt[k]%1000000007

    def securityCheck(self, capacities: List[int], k: int) -> int:
        cnt1 = capacities.count(1)
        nums = [x-1 for x in capacities if x>1] # 找和为k的子数组个数
        return (self.subarraySum(nums,k) * pow(2,cnt1,1000000007))%1000000007


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.securityCheck(*data)


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
        # [[4,3,2,2],6],
        [[1],0],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
