### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_41. 数据流中的中位数
```



### 正文

```
### Offer_day17_41. 数据流中的中位数






代码：

​```python
import time
from typing import List


class MedianFinder:
    def __init__(self):
        from sortedcontainers import SortedList
        self.length = 0
        self.datas = SortedList()
        self.mid = None

    def addNum(self, num: int) -> None:
        self.length+=1
        self.datas.add(num)
        self.mid = None

    def findMedian(self) -> float:
        if self.mid:
            return self.mid
        else:
            if self.length%2:
                self.mid = self.datas[(self.length-1)//2]
            else:
                right = self.length//2
                self.mid = sum(self.datas[right-1:right+1])/2
            return self.mid


def test(data_test):
    s = Solution()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = MedianFinder(*data_test[1][0])
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
​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总_卷子的博客-CSDN博客](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    