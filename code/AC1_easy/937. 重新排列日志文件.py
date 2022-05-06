# -*- coding: utf-8 -*-
# @Time    : 2022/5/3 11:19
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 937. 重新排列日志文件.py
# @Software: PyCharm 
# ===================================
"""给你一个日志数组 logs。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 标识符 。

有两种不同类型的日志：

字母日志：除标识符之外，所有字均由小写字母组成
数字日志：除标识符之外，所有字均由数字组成
请按下述规则将日志重新排序：

所有 字母日志 都排在 数字日志 之前。
字母日志 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
数字日志 应该保留原来的相对顺序。
返回日志的最终顺序。

 

示例 1：

输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
解释：
字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。
示例 2：

输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

提示：

1 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] 中，字与字之间都用 单个 空格分隔
题目数据保证 logs[i] 都有一个标识符，并且在标识符之后至少存在一个字

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-data-in-log-files
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(log: str) -> tuple:
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1,)
        logs.sort(key=trans)
        return logs



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
