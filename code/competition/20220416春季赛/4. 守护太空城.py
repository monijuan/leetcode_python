# -*- coding: utf-8 -*-
# @Time    : 2022/4/16 14:57
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 4. 守护太空城.py
# @Software: PyCharm 
# ===================================
"""各位勇者请注意，力扣太空城发布陨石雨红色预警。

太空城中的一些舱室将要受到陨石雨的冲击，这些舱室按照编号 0 ~ N 的顺序依次排列。为了阻挡陨石损毁舱室，太空城可以使用能量展开防护屏障，具体消耗如下：

选择一个舱室开启屏障，能量消耗为 2
选择相邻两个舱室开启联合屏障，能量消耗为 3
对于已开启的屏障，多维持一时刻，能量消耗为 1
已知陨石雨的影响范围和到达时刻，time[i] 和 position[i] 分别表示该陨石的到达时刻和冲击位置。请返回太空舱能够守护所有舱室所需要的最少能量。

注意：

同一时间，一个舱室不能被多个屏障覆盖
陨石雨仅在到达时刻对冲击位置处的舱室有影响
示例 1：

输入：time = [1,2,1], position = [6,3,3]

输出：5

解释：
时刻 1，分别开启编号 3、6 舱室的屏障，能量消耗 2*2 = 4
时刻 2，维持编号 3 舱室的屏障，能量消耗 1
因此，最少需要能量 5

示例 2：

输入：time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]

输出：9

解释：
时刻 1，开启编号 1、2 舱室的联合屏障，能量消耗 3
时刻 1，开启编号 3 舱室的屏障，能量消耗 2
时刻 2，维持编号 1、2 舱室的联合屏障，能量消耗 1
时刻 3，维持编号 1、2 舱室的联合屏障，能量消耗 1
时刻 5，重新开启编号 3 舱室的联合屏障，能量消耗 2
因此，最少需要能量 9

提示：

1 <= time.length == position.length <= 500
1 <= time[i] <= 5
0 <= position[i] <= 100
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        pass

    def getResult(self,args):
        return


def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = Solution(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
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
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
