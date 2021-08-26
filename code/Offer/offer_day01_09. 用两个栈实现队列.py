# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 10:37
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : offer_day01_09. 用两个栈实现队列.py
# @Software: PyCharm
# ===================================
"""用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

 

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
from typing import List


class CQueue:
    def __init__(self):
        """
        # Your CQueue object will be instantiated and called as such:
        # obj = CQueue()
        # obj.appendTail(value)
        # param_2 = obj.deleteHead()
        """
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value: int) -> None:
        self.stack_1.append(value)
        return None

    def deleteHead(self) -> int:
        if len(self.stack_2):       # 2还有，之前的没出完
            out = self.stack_2[-1]
            self.stack_2 = self.stack_2[:-1]
        elif len(self.stack_1):     # 1还有，把1的逆序放入2
            out = self.stack_1[0]
            self.stack_2 = self.stack_1[:0:-1]
            self.stack_1.clear()
        else:                       # 都为空，返回-1
            out = -1
        return out


def test(data_test):
    result = [None]
    obj = CQueue()
    for value in data_test[1::]:
        # print('-'*50)
        if len(value):
            res = obj.appendTail(value)
        else:
            res = obj.deleteHead()
        # print('value',value,'res',res)
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        # [[],[3],[],[]],   # [null,null,3,-1]
        [[],[],[12],[],[10],[9],[2],[42],[],[20],[],[1],[8],[20],[1],[11],[2],[],[],[],[]],
        # [[],[],[12],[],[10],[9],[],[],[],[20],[],[1],[8],[20],[1],[11],[2],[],[],[],[]], # [null,-1,null,12,null,null,10,9,-1,null,20,null,null,null,null,null,null,1,8,20,1]
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
