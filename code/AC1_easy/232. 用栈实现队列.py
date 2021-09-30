# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 14:39
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 232. 用栈实现队列.py
# @Software: PyCharm
# ===================================
"""请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
 

说明：

你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

进阶：

你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
 

示例：

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

提示：

1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
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

    def peek(self) -> int:
        if len(self.stack_2):       # 2还有，之前的没出完
            out = self.stack_2[-1]
        elif len(self.stack_1):     # 1还有，把1的逆序放入2
            out = self.stack_1[0]
        else:                       # 都为空，返回-1
            out = -1
        return out

    def empty(self) -> bool:
        return len(self.stack_1) ==0 and len(self.stack_2) ==0


def test(data_test):
    s = MyQueue()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = MyQueue(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        [["MyQueue","push","push","peek","pop","empty"],[[],[1],[2],[],[],[]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
