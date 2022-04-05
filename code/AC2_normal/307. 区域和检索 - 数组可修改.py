# -*- coding: utf-8 -*-
# @Time    : 2022/4/4 19:06
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 307. 区域和检索 - 数组可修改.py
# @Software: PyCharm 
# ===================================
"""给你一个数组 nums ，请你完成两类查询。

其中一类查询要求 更新 数组 nums 下标对应的值
另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
实现 NumArray 类：

NumArray(int[] nums) 用整数数组 nums 初始化对象
void update(int index, int val) 将 nums[index] 的值 更新 为 val
int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
 

示例 1：

输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
 

提示：

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
调用 update 和 sumRange 方法次数不大于 3 * 104 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *
class tree_树状数组:
    def __init__(self, n):
        self.n = n + 5
        self.sum = [0 for _ in range(n + 10)]
        self.ntimessum = [0 for _ in range(n + 10)]

    def _lowbit(self, x):
        return x & (-x)

    ### region 单点更新
    def add_pos(self, pos, k):
        """pos 单点更新 k"""
        x = pos
        while pos <= self.n:
            self.sum[pos] += k
            self.ntimessum[pos] += k * (x - 1)
            pos += self._lowbit(pos)

    def sum_pos_single(self, pos):
        """ 单点更新：1~pos 区间求和 """
        if not pos: return 0
        ret = 0
        while pos:
            ret += self.sum[pos]
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_single(self, l, r):
        """ 单点更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_single(r) - self.sum_pos_single(l - 1)

    def get_pos(self, pos):
        """ 单点更新：pos 单点查询 """
        return self.sum_pos_single(pos) - self.sum_pos_single(pos - 1)
    ####### endregion 单点更新

    ### region 区间更新
    def add_lr(self, l, r, k):
        """l~r 区间更新 k"""
        self.add_pos(l, k)
        self.add_pos(r + 1, -k)

    def sum_pos_internal(self, pos):
        """ 区间更新：1~pos 区间求和 """
        if not pos:
            return 0
        ret = 0
        x = pos
        while pos:
            ret += x * self.sum[pos] - self.ntimessum[pos]
            pos -= self._lowbit(pos)
        return ret

    def sum_lr_internal(self, l, r):
        """ 区间更新：l~r 区间求和 """
        if l > r: return 0
        return self.sum_pos_internal(r) - self.sum_pos_internal(l - 1)

    def get_sums(self):
        """ 区间更新：计算所有[0,i]的求和"""
        return [self.sum_pos_internal(i) for i in range(1,self.n)]

    def get_scores(self):
        """ 区间更新：计算每一位的值"""
        sums = [self.sum_pos_internal(i) for i in range(1,self.n)]
        return [s-sums[i-1] if i>0 else s for i,s in enumerate(sums)]
    ####### endregion 区间更新

class NumArray:

    def __init__(self, nums: List[int]):
        self.length = len(nums)+1
        self.tree = tree_树状数组(self.length)
        for i,n in enumerate(nums):
            self.tree.add_pos(i+1,n)

    def update(self, index: int, val: int) -> None:
        old = self.tree.get_pos(index+1)
        self.tree.add_pos(index+1,val-old)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sum_pos_single(right+1)-self.tree.sum_pos_single(left)




def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)

def test_obj(data_test):
    result = [None]
    obj = NumArray(*data_test[1][0])
    for fun,data in zip(data_test[0][1::],data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result

if __name__ == '__main__':
    datas = [
        [["NumArray","sumRange","update","sumRange"],[[[1,3,5]],[0,2],[1,2],[0,2]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
