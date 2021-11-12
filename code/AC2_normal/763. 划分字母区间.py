# -*- coding: utf-8 -*-
# @Time    : 2021/11/12 9:32
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 763. 划分字母区间.py
# @Software: PyCharm
# ===================================
"""字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
 

提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        """每次找到最大id，等id不变了说明切割完了，有点像层序遍历的思路"""
        pass

    def partitionLabels(self, s: str) -> List[int]:
        char_maxid = dict()
        for id,char in enumerate(s):
            char_maxid[char] = id

        res = []
        start_id  = 0
        while start_id<len(s):
            end_id = -1
            end_id_new = start_id
            while end_id!=end_id_new:
                end_id = end_id_new
                together_char = set(s[start_id:end_id+1])
                end_id_new = max([char_maxid[char] for char in together_char])
            res.append(end_id_new-start_id+1)
            start_id = end_id_new+1
        return res


def test(data_test):
    s = Solution()
    return s.partitionLabels(*data_test)


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
        ["ababcbacadefegdehijhklij"],
        ["eccbbbbdec"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
