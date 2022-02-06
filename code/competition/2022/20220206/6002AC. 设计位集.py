# -*- coding: utf-8 -*-
# @Time    : 2022/2/6 10:23
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6002AC. 设计位集.py
# @Software: PyCharm 
# ===================================
"""位集 Bitset 是一种能以紧凑形式存储位的数据结构。

请你实现 Bitset 类。

Bitset(int size) 用 size 个位初始化 Bitset ，所有位都是 0 。
void fix(int idx) 将下标为 idx 的位上的值更新为 1 。如果值已经是 1 ，则不会发生任何改变。
void unfix(int idx) 将下标为 idx 的位上的值更新为 0 。如果值已经是 0 ，则不会发生任何改变。
void flip() 翻转 Bitset 中每一位上的值。换句话说，所有值为 0 的位将会变成 1 ，反之亦然。
boolean all() 检查 Bitset 中 每一位 的值是否都是 1 。如果满足此条件，返回 true ；否则，返回 false 。
boolean one() 检查 Bitset 中 是否 至少一位 的值是 1 。如果满足此条件，返回 true ；否则，返回 false 。
int count() 返回 Bitset 中值为 1 的位的 总数 。
String toString() 返回 Bitset 的当前组成情况。注意，在结果字符串中，第 i 个下标处的字符应该与 Bitset 中的第 i 位一致。


示例：

输入
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
输出
[null, null, null, null, false, null, null, true, null, 2, "01010"]

解释
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // 将 idx = 3 处的值更新为 1 ，此时 bitset = "00010" 。
bs.fix(1);     // 将 idx = 1 处的值更新为 1 ，此时 bitset = "01010" 。
bs.flip();     // 翻转每一位上的值，此时 bitset = "10101" 。
bs.all();      // 返回 False ，bitset 中的值不全为 1 。
bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "00101" 。
bs.flip();     // 翻转每一位上的值，此时 bitset = "11010" 。
bs.one();      // 返回 True ，至少存在一位的值为 1 。
bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "01010" 。
bs.count();    // 返回 2 ，当前有 2 位的值为 1 。
bs.toString(); // 返回 "01010" ，即 bitset 的当前组成情况。


提示：

1 <= size <= 105
0 <= idx <= size - 1
至多调用 fix、unfix、flip、all、one、count 和 toString 方法 总共 105 次
至少调用 all、one、count 或 toString 方法一次
至多调用 toString 方法 5 次
"""
from leetcode_python.utils import *


class Bitsetf:
    def __init__(self, size: int):
        self.nums = [False]*size
        self.f =  False

    def fix(self, idx: int) -> None:
        self.nums[idx]=True

    def unfix(self, idx: int) -> None:
        self.nums[idx]=False

    def flip(self) -> None:
        # self.nums = [not x for x in self.nums]
        self.f=not self.f

    def all(self) -> bool:
        if self.f:
            return not any(self.nums)
        else:
            return all(self.nums)

    def one(self) -> bool:
        if self.f:
            return not all(self.nums)
        else:
            return any(self.nums)

    def count(self) -> int:
        if self.f:
            return self.nums.count(False)
        else:
            return self.nums.count(True)

    def toString(self) -> str:
        if self.f:
            return ''.join([str(int(not x)) for x in self.nums])
        else:
            return ''.join([str(int(x))for x in self.nums])

class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.falseid = set(range(size))
        self.trueid = set()
        self.f=False

    def fix(self, idx: int) -> None:
        if idx in self.falseid:
            self.falseid.remove(idx)
        self.trueid.add(idx)

    def unfix(self, idx: int) -> None:
        if idx in self.trueid:
            self.trueid.remove(idx)
            self.falseid.add(idx)

    def flip(self) -> None:
        self.trueid,self.falseid = self.falseid,self.trueid

    def all(self) -> bool:
        return len(self.falseid)==0

    def one(self) -> bool:
        return len(self.trueid)>0


    def count(self) -> int:
        return len(self.trueid)

    def toString(self) -> str:
        return ''.join('1' if x in self.trueid else '0' for x in range(self.size))



# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()

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

