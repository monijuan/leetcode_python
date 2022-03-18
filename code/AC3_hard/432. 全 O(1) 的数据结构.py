# -*- coding: utf-8 -*-
# @Time    : 2022/3/16 8:46
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 432. 全 O(1) 的数据结构.py
# @Software: PyCharm
# ===================================
"""请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 AllOne 类：

AllOne() 初始化数据结构的对象。
inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。
 

示例：

输入
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"
 

提示：

1 <= key.length <= 10
key 由小写英文字母组成
测试用例保证：在每次调用 dec 时，数据结构中总存在 key
最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 104 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-oone-data-structure
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from leetcode_python.utils import *

from sortedcontainers import SortedDict
class AllOne:
    def __init__(self):
        self.key_cnt = defaultdict(int)
        self.cnt_keys = defaultdict(list)
        self.maxcnt = 0

    def inc(self, key: str) -> None:
        if key in self.key_cnt:
            self.cnt_keys[self.key_cnt[key]].remove(key)
            if 0==len(self.cnt_keys[self.key_cnt[key]]):
                self.cnt_keys.pop(self.key_cnt[key])
        self.key_cnt[key]+=1
        self.cnt_keys[self.key_cnt[key]].append(key)
        self.maxcnt = max(self.maxcnt,self.key_cnt[key])

    def dec(self, key: str) -> None:
        oldcnt = self.key_cnt[key]
        if oldcnt==1:
            self.key_cnt.pop(key)
            self.cnt_keys[oldcnt].remove(key)
        else:
            self.key_cnt[key]-=1
            self.cnt_keys[oldcnt].remove(key)
            self.cnt_keys[oldcnt-1].append(key)

        if 0==len(self.cnt_keys[oldcnt]):
            self.cnt_keys.pop(oldcnt)
            if self.maxcnt == oldcnt:
                self.maxcnt = max(self.cnt_keys.keys()) if self.cnt_keys.keys() else None

    def getMaxKey(self) -> str:
        return self.cnt_keys[self.maxcnt][0] if self.maxcnt else ''

    def getMinKey(self) -> str:
        return self.cnt_keys[min(self.cnt_keys.keys())][0] if self.maxcnt else ''


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.getResult(*data)


def test_obj(data_test):
    result = [None]
    obj = AllOne(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
    return result


if __name__ == '__main__':
    datas = [
        # [["AllOne","inc","inc","getMaxKey","getMinKey","inc","getMaxKey","getMinKey"],[[],["hello"],["hello"],[],[],["leet"],[],[]]],
        # [["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"],[[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]],
        [["AllOne","inc","inc","inc","inc","inc","dec","dec","getMaxKey","getMinKey"],[[],["a"],["b"],["b"],["b"],["b"],["b"],["b"],[],[]]],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
