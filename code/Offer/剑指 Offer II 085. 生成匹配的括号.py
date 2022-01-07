# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 9:00
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 剑指 Offer II 085. 生成匹配的括号.py
# @Software: PyCharm
# ===================================
"""正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
 

注意：本题与主站 22 题相同： https://leetcode-cn.com/problems/generate-parentheses/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/IDBivT
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def dfs(self,s:str):
        num_left=s.count('(')
        num_right=s.count(')')
        if self.n==num_left and self.n==num_right:
            self.res.append(s)
        else:
            if self.n>num_left:self.dfs(s+'(')
            if num_left>num_right:self.dfs(s+')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.n=n
        self.res=[]
        self.dfs('')
        return self.res

class Solution_慢:
    def dfs(self,s,cl,cr):
        if self.n==cl and self.n==cr:
            self.res.append(s)
        else:
            if self.n>cl:self.dfs(s+'(',cl+1,cr)
            if cl>cr:self.dfs(s+')',cl,cr+1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.n=n
        self.res=[]
        self.dfs('',0,0)
        return self.res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [list2node(data_test[0])]  # list转node
    return s.getResult(*data)


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
        [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
