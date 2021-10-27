# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 14:03
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 301. 删除无效的括号.py
# @Software: PyCharm
# ===================================
"""给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。

 

示例 1：

输入：s = "()())()"
输出：["(())()","()()()"]
示例 2：

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]
示例 3：

输入：s = ")("
输出：[""]
 

提示：

1 <= s.length <= 25
s 由小写英文字母以及括号 '(' 和 ')' 组成
s 中至多含 20 个括号

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        self.res_cut = set()
        pass

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.s = s
        self.length = len(s)
        # 计算需要去除'（'和'）'的最小数目
        left_cut,right_cut = 0,0
        for char in s:
            if '('==char:left_cut+=1
            elif ')'==char and 0==left_cut:right_cut+=1
            elif ')'==char:left_cut-=1
        self.length_out = len(s) - left_cut - right_cut
        self.dfs(left_cut,right_cut) # dfs遍历所有去除后的情况，方法是一个个字符往里插入
        return list(self.res_cut) if len(self.res_cut) else ['']


    def dfs(self,left_cut,right_cut,left_now=0,right_now=0,index = 0,s_temp=''):
        """
        计算需要去除左括号的数量和右括号的数量，遍历每个字符，判断是否保留，一共分五种情况：
            - 如果是（：保留这个括号（左括号都可以保留）
            - 如果是）：不保留这个括号（还可去除左括号）
            - 如果是（：保留这个括号（右边更多的话肯定不合法）
            - 如果是）：不保留这个括号（还可去除右括号）
            - 其他字符：保留
        :param left_cut:    需要裁剪（的数量
        :param right_cut:   需要裁剪）的数量
        :param left_now:        当前（的数量
        :param right_now:       当前）的数量
        :param index:               当前插入字符在原字符串的下标
        :param s_temp:              当前字符串
        :return:None
        """
        # 边界条件：字符串长度添加到和结果一样了
        # print(len(s_temp),self.length_out,left_cut,right_cut,s_temp)
        # if len(s_temp)>=self.length_out:
        if index==self.length:
            if 0==left_cut and 0==right_cut:
                self.res_cut.add(s_temp)
            return

        # 长度不够，说明还需要继续添加
        char_now = self.s[index]

        if '('==char_now:
            self.dfs(left_cut, right_cut, left_now+1, right_now, index + 1, s_temp + char_now)    # 保留这个括号（左括号都可以保留）
            if left_cut > 0: self.dfs(left_cut - 1, right_cut, left_now, right_now, index + 1, s_temp)  # 不保留这个括号（还可去除左括号）
        elif ')'==char_now:
            if left_now>right_now: self.dfs(left_cut, right_cut, left_now, right_now+1, index + 1, s_temp + char_now) # 保留这个括号（右边更多的话肯定不合法）
            if right_cut>0:self.dfs(left_cut, right_cut - 1, left_now, right_now, index + 1, s_temp)  # 不保留这个括号（还可去除右括号）
        else:
            self.dfs(left_cut, right_cut, left_now, right_now, index + 1, s_temp + char_now)    # 保留所有不是括号






def test(data_test):
    s = Solution()
    return s.removeInvalidParentheses(*data_test)


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

datas = [
    ["(a)())()"],
    ["()())()"],
    [")("],
    ["x("],
]

if __name__ == '__main__':
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
