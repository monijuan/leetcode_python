# -*- coding: utf-8 -*-
# @Time    : 2021/11/11 15:54
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 376. 摆动序列.py
# @Software: PyCharm
# ===================================
"""如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

 

示例 1：

输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
示例 2：

输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
示例 3：

输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2
 

提示：

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
 

进阶：你能否用 O(n) 时间复杂度完成此题?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """
        我本来想的思路是：
            两个队列，一个存放此时应该递增，一格存放此时应该递减
            对于应该递增的：
                如果更大：正常插入
                如果更小，并且也比倒数第2个数更小，为了使范围更广，则可以替换最后一个数
            对于应该递减的：
                如果更小：正常插入
                如果更大，并且也比倒数第2个数更大，为了使范围更广，则可以替换最后一个数
        但是后来发现好像不能处理连续变大或连续变小的情况。
        其实本身并不需要保存所有数，只需要记录变大变小的长度，那么只要计算每个数和前一个数的差：
            如果为正，说明递增的长度 = 之前递减的+1
            如果为负，说明递减的长度 = 之前递增的+1
        就算连续递增、连续递减，之前的另一个长度不会受到影响，而且这样也不需要考虑范围变化了
        """
        pass

    def wiggleMaxLength(self, nums: List[int]) -> int:
        len_p=len_n=0
        for id,num in enumerate(nums):
            if 0==id:
                len_p=len_n=1
            else:
                diff = num-nums[id-1]
                if diff>0:
                    len_p=len_n+1
                elif diff<0:
                    len_n=len_p+1
        return max(len_n,len_p)

    def wiggleMaxLength_wrong(self, nums: List[int]) -> int:
        dp_p,dp_n=[],[]
        for id,num in enumerate(nums):
            if id==0:
                dp_p.append(num)
                dp_n.append(num)
                continue
            if num>dp_p[-1]:
                dp_p.append(num)
            elif num<dp_p[-1] and (id==1 or num>dp_p[-2]):
                dp_p[-1]=num
            if num<dp_n[-1]:
                dp_n.append(num)
            elif num>dp_n[-1] and (id==1 or num>dp_p[-2]):
                dp_p[-1]=num
            dp_p,dp_n = dp_n,dp_p
            print('p',dp_p)
            print('n',dp_n)
        return max(len(dp_p),len(dp_n))


def test(data_test):
    s = Solution()
    return s.wiggleMaxLength(*data_test)


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
        [[1,17,5,10,13,15,10,5,16,8]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
