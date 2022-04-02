# -*- coding: utf-8 -*-
# @Time    : 2022/4/1 8:32
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 954. 二倍数对数组.py
# @Software: PyCharm 
# ===================================
"""给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

 

示例 1：

输入：arr = [3,1,3,6]
输出：false
示例 2：

输入：arr = [2,1,2,6]
输出：false
示例 3：

输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
 

提示：

0 <= arr.length <= 3 * 104
arr.length 是偶数
-105 <= arr[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for num in sorted(cnt.keys(),key=lambda x:abs(x)):
            if cnt[num]:
                if cnt.get(num*2,0)>=cnt[num]:
                    cnt[num*2]-=cnt[num]
                else:
                    return False
        return True



def test(data_test):
    s = Solution()
    data = data_test    # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.canReorderDoubled(*data)

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
        [[4,-2,2,-4]],
        # [[-5,-3]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
