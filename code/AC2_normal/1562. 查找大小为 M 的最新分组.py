# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 17:59
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 1562. 查找大小为 M 的最新分组.py
# @Software: PyCharm 
# ===================================
"""给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。

在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。

给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。

返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。

 

示例 1：

输入：arr = [3,5,1,2,4], m = 1
输出：4
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："00101"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："11101"，由 1 构成的组：["111", "1"]
步骤 5："11111"，由 1 构成的组：["11111"]
存在长度为 1 的一组 1 的最后步骤是步骤 4 。
示例 2：

输入：arr = [3,1,5,4,2], m = 2
输出：-1
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："10100"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："10111"，由 1 构成的组：["1", "111"]
步骤 5："11111"，由 1 构成的组：["11111"]
不管是哪一步骤都无法形成长度为 2 的一组 1 。
示例 3：

输入：arr = [1], m = 1
输出：1
示例 4：

输入：arr = [2,1], m = 2
输出：2
 

提示：

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
arr 中的所有整数 互不相同
1 <= m <= arr.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-latest-group-of-size-m
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from leetcode_python.utils import *


class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]  # x的直接老板是谁（不是掌门，不是幕后boss ）
        self.sz = [0 for x in range(n)]  # 不同之处  等函数中置1了,从说明这是个人  每个人能管几个人  能管自己也算1个
        self.part = n  # 江湖上有几个门派

    def Find(self, x: int) -> int:  # 找x所在门派的 掌门（终极boss，门派老大）
        if self.parent[x] == x:
            return x
        return self.Find(self.parent[x])

    def Union(self, x: int, y: int) -> bool:  # 合并两个门派
        root_x = self.Find(x)  # x所在门派的掌门
        root_y = self.Find(y)  # y所在门派的掌门
        if root_x == root_y:  # 如果是同一个人  不用合并了  本就是同门
            return False
        if self.sz[root_x] > self.sz[root_y]:  # root_x 手下的人多
            root_x, root_y = root_y, root_x  # 为了代码写起来简洁  不然要写个else root_y合并到root_x门下
        self.parent[root_x] = root_y  # root_x带着门派投靠到root_y门下  root_x认root_y做老板
        self.sz[root_y] += self.sz[root_x]  # root_y手下的人马 更多了  把新增的人马数统计好
        self.part -= 1  # 江湖上从此少了一个门派
        return True

    def inthesamepart(self, x: int, y: int) -> bool:  # 判断 x y 在不在同一个门派
        root_x = self.Find(x)
        root_y = self.Find(y)
        return root_x == root_y

    def getpartsize(self, x: int) -> int:  # 判断 x 所在的门派， 有多少人
        root_x = self.Find(x)
        return self.sz[root_x]  # 其实就是  掌门手下有多少人马（包含掌门自己）


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        UF = UnionFind(n)
        bit = [0 for _ in range(n)]  # 记录哪位置1了 哪位还是0
        res = -1
        step = 0
        m_Len = set()  # 长度为m的root_x
        for digit in arr:  # digit从1开始
            x = digit - 1  # 而数组 并查集 从0开始
            pre, nxt = x - 1, x + 1  # 前 后
            bit[x] = 1  # 置1
            UF.sz[x] = 1  # 并查集中 x所管辖的尺寸置1（先能管自己）
            if 0 <= pre < n and bit[pre] == 1:
                UF.Union(pre, x)  # 前后能连起来 就Union
            if 0 <= nxt < n and bit[nxt] == 1:
                UF.Union(x, nxt)

            root_x = UF.Find(x)
            if UF.sz[root_x] == m:  # 每个门派 把自己掌门放进去就ok
                m_Len.add(root_x)  # 掌门代表这个门派

            remove_keys = set()
            for k in m_Len:
                if UF.getpartsize(k) != m:  # 可能被合并了 或者吞并了别人  但自己可能变大了
                    remove_keys.add(k)  # 记下来  待会儿 移走
            for k in remove_keys:
                m_Len.remove(k)  # 正式移走

            step += 1  # 更新step
            if len(m_Len) > 0:
                res = step
        return res


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
