# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 10:38
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : LCP 08. 剧情触发时间.py
# @Software: PyCharm
# ===================================
"""在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（C），资源储备（R）以及人口数量（H）。在游戏开始时（第 0 天），三种属性的值均为 0。

随着游戏进程的进行，每一天玩家的三种属性都会对应增加，我们用一个二维数组 increase 来表示每天的增加情况。这个二维数组的每个元素是一个长度为 3 的一维数组，例如 [[1,2,1],[3,4,2]] 表示第一天三种属性分别增加 1,2,1 而第二天分别增加 3,4,2。

所有剧情的触发条件也用一个二维数组 requirements 表示。这个二维数组的每个元素是一个长度为 3 的一维数组，对于某个剧情的触发条件 c[i], r[i], h[i]，如果当前 C >= c[i] 且 R >= r[i] 且 H >= h[i] ，则剧情会被触发。

根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。

示例 1：

输入： increase = [[2,8,4],[2,5,0],[10,9,8]] requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]

输出: [2,-1,3,-1]

解释：

初始时，C = 0，R = 0，H = 0

第 1 天，C = 2，R = 8，H = 4

第 2 天，C = 4，R = 13，H = 4，此时触发剧情 0

第 3 天，C = 14，R = 22，H = 12，此时触发剧情 2

剧情 1 和 3 无法触发。

示例 2：

输入： increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]] requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]

输出: [-1,4,3,3,3]

示例 3：

输入： increase = [[1,1,1]] requirements = [[0,0,0]]

输出: [0]

限制：

1 <= increase.length <= 10000
1 <= requirements.length <= 100000
0 <= increase[i] <= 10
0 <= requirements[i] <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-qing-hong-fa-shi-jian
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        参考官解的思路：统计到达所有属性所需要的天数，达到可以随机存取的效果，最后查询就很方便了
        超时case：https://leetcode-cn.com/submissions/detail/238727420/testcase/
        """
        pass

    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        self.len_day = len(increase)
        # 统计每个属性对应的天数
        increase.insert(0,[0,0,0]) # 补充开局[0,0,0]
        CRH,CRH_last = [0,0,0],[0,0,0]

        # 通过字典映射加速
        C_day_dict={0:0}
        R_day_dict={0:0}
        H_day_dict={0:0}
        for day,inc in enumerate(increase):
            if day==0:continue # 开局仍然是[0,0,0]
            CRH = [a+b for a,b in zip(CRH,increase[day])]
            for value in range(CRH_last[0]+1,CRH[0]+1):
                C_day_dict[value]=day
            for value in range(CRH_last[1]+1,CRH[1]+1):
                R_day_dict[value]=day
            for value in range(CRH_last[2]+1,CRH[2]+1):
                H_day_dict[value]=day
            CRH_last = CRH

        # 判断每个剧情。此时CRH是最大属性
        res = []
        for req in requirements:
            day_need = [C_day_dict.get(req[0],-1),
                        R_day_dict.get(req[1],-1),
                        H_day_dict.get(req[2],-1),]
            if -1 in day_need:
                res.append(-1)
            else:
                res.append(max(day_need))
        return res


class Solution_没有去注释:
    def __init__(self):
        """
        参考官解的思路：统计到达所有属性所需要的天数，达到可以随机存取的效果，最后查询就很方便了
        超时case：https://leetcode-cn.com/submissions/detail/238727420/testcase/
        """
        pass

    def __find_day_二分查找超时(self,crh,req):
        CRH_day = self.__getattribute__(crh)
        # print(f'find day {crh}:{CRH_day}, req:{req}')
        if CRH_day[-1]<req:return -1
        # 二分查找是那一天
        left,right = 0,self.len_day
        mid_day = left+(right-left)//2
        while left<right:
            if CRH_day[mid_day]==req:
                return mid_day
            elif CRH_day[mid_day]<req:
                left = mid_day+1
            else:
                if left+1==right:return right
                right = mid_day
        return right

    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        self.len_day = len(increase)
        # 统计每个属性对应的天数
        self.C_day,self.R_day,self.H_day = [],[],[]
        increase.insert(0,[0,0,0]) # 补充开局[0,0,0]
        CRH,CRH_last = [0,0,0],[0,0,0]
        ######## 二分查找，仍然超时
        # for day,inc in enumerate(increase):
        #     CRH = [a+b for a,b in zip(CRH,increase[day])]# 开局仍然是[0,0,0]
        #     self.C_day.append(CRH[0])
        #     self.R_day.append(CRH[1])
        #     self.H_day.append(CRH[2])

        ######## 通过字典映射加速
        C_day_dict={0:0}
        R_day_dict={0:0}
        H_day_dict={0:0}
        for day,inc in enumerate(increase):
            if day==0:continue# 开局仍然是[0,0,0]
            CRH = [a+b for a,b in zip(CRH,increase[day])]
            for value in range(CRH_last[0]+1,CRH[0]+1):
                C_day_dict[value]=day
            for value in range(CRH_last[1]+1,CRH[1]+1):
                R_day_dict[value]=day
            for value in range(CRH_last[2]+1,CRH[2]+1):
                H_day_dict[value]=day
            CRH_last = CRH
        # print(CRH)
        # print(C_day_dict.values())
        # print(R_day_dict.values())
        # print(H_day_dict.values())
        ########################


        # 判断每个剧情。此时CRH是最大属性
        res = []
        for req in requirements:
            # day_need = [self.__find_day_二分查找超时('C_day',req[0]),
            #             self.__find_day_二分查找超时('R_day',req[1]),
            #             self.__find_day_二分查找超时('H_day',req[2]),]
            day_need = [C_day_dict.get(req[0],-1),
                        R_day_dict.get(req[1],-1),
                        H_day_dict.get(req[2],-1),]
            # print(req,day_need)
            if -1 in day_need:
                res.append(-1)
            else:
                res.append(max(day_need))
        return res


    def getTriggerTime_超时(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        increase.insert(0,[0,0,0]) # 补充开局[0,0,0]
        len_day,len_req = len(increase),len(requirements)
        CRH = [0,0,0]
        res = [-1] * len_req
        for day in range(len_day):
            CRH = [a+b for a,b in zip(CRH,increase[day])]# 开局仍然是[0,0,0]
            # 检查是否触发剧情
            for id in range(len_req):
                if -1==res[id] and all([a>=b for a,b in zip(CRH,requirements[id])]):
                    res[id]=day
        return res


def test(data_test):
    s = Solution()
    return s.getTriggerTime(*data_test),s.getTriggerTime_超时(*data_test)


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
        # [[[2,8,4],[2,5,0],[10,9,8]],[[2,11,3],[15,10,7],[9,17,12],[8,1,14]]],
        [[[6,3,4],[6,7,2]],[[0,13,14],[0,5,5],[0,4,18],[4,3,4]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
