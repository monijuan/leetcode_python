### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_65. 不用加减乘除做加法
```



### 正文

```
### Offer_day21_65. 不用加减乘除做加法

写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def add(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        a &= x
        b &= x
        while b != 0:
            carry = (a & b) << 1 & x
            a ^= b
            b = carry
        return a if a<=0x7fffffff else ~(a^x)

class Solution1:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


def test(data_test):
    s = Solution()
    return s.add(*data_test)


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
        [1,1],
        [-1,2],
        [0,-4],
        # [64,128],
        # [188,1576],
        # [182348,1523476],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')

​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总_卷子的博客-CSDN博客](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    