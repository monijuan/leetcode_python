# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 15:59
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 352. 将数据流变为多个不相交区间.py
# @Software: PyCharm
# ===================================
""" 给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

实现 SummaryRanges 类：

SummaryRanges() 使用一个空数据流初始化对象。
void addNum(int val) 向数据流中加入整数 val 。
int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
 

示例：

输入：
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出：
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释：
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // 返回 [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
 

提示：

0 <= val <= 104
最多调用 addNum 和 getIntervals 方法 3 * 104 次
 

进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *
from sortedcontainers import SortedSet

class SummaryRanges:
    def __init__(self):
        from sortedcontainers import SortedSet
        self.myright = [i for i in range(10002)]
        self.sortednum = SortedSet()

    def addNum(self, val: int) -> None:
        self.sortednum.add(val)
        self.myright[val] = self.myright[val+1]

    def findRightPlus(self,val)->int:
        """找到val开始往右连续存在于sortednum中的数"""
        if val==self.myright[val]:return val
        self.myright[val]=self.findRightPlus(self.myright[val]) # 其实递归是从右往左找
        return self.myright[val]

    def getIntervals(self) -> List[List[int]]:
        res = []
        for num in self.sortednum:
            if res and num<=res[-1][1]:continue
            else:res.append([num,self.findRightPlus(num)-1])
        return res



def test(data_test):
    s = SummaryRanges()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = SummaryRanges(*data_test[1][0])
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
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
