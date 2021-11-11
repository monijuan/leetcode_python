### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_50. 第一个只出现一次的字符
```



### 正文

```
### Offer_day05_50. 第一个只出现一次的字符

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
 

限制：

0 <= s 的长度 <= 50000

通过次数139,668提交次数227,462
请问您在哪类招聘中遇到此题

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def firstUniqChar(self, s: str) -> str:
        short = s
        while len(short):
            print(short)
            if len(short)==1:return short
            elif short[0] not in short[1:]:return short[0]
            else:
                short = short.replace(short[0],'')
        return ' '


def test(data_test):
    s = Solution()
    return s.firstUniqChar(*data_test)


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
        ["leetcode"],
        ["abaccdeff"],
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
    