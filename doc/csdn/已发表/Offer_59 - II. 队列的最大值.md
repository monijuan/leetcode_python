### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_59 - II. 队列的最大值
```



### 正文

```
### Offer_day27_59 - II. 队列的最大值






代码：

​```python
from leetcode_python.utils import *


class MaxQueue:

    def __init__(self):
        self.max = None
        self.num = 0
        self.queue = []

    def max_value(self) -> int:
        if self.num and self.max:
            return self.max
        elif self.num:
            self.max=max(self.queue)
            return self.max
        else:
            return -1

    def push_back(self, value: int) -> None:
        if self.num<=0:
            self.max=value
        elif self.max:
            self.max=max(self.max,value)
        self.num+=1
        self.queue.append(value)

    def pop_front(self) -> int:
        if self.num<=0:
            return -1
        res = self.queue[0]
        if res==self.max:
            self.max=None
        self.queue.pop(0)
        self.num-=1
        return res


def test(data_test):
    s = MaxQueue()
    return s.getResult(*data_test)


def test_obj(data_test):
    result = [None]
    obj = MaxQueue(*data_test[1][0])
    for fun, data in zip(data_test[0][1::], data_test[1][1::]):
        if data:
            res = obj.__getattribute__(fun)(*data)
        else:
            res = obj.__getattribute__(fun)()
        result.append(res)
        # print(result,fun, data,obj.queue)
        print(result[-5:],fun, data,obj.queue)
    return result


if __name__ == '__main__':
    datas = [
        [["MaxQueue","push_back","push_back","max_value","pop_front","max_value"],[[],[1],[2],[],[],[]]],
        [["MaxQueue","max_value","pop_front","pop_front","push_back","push_back","push_back","pop_front","push_back","pop_front"],[[],[],[],[],[94],[16],[89],[],[22],[]]],
        [["MaxQueue","max_value","pop_front","max_value","push_back","max_value","pop_front","max_value","pop_front","push_back","pop_front","pop_front","pop_front","push_back","pop_front","max_value","pop_front","max_value","push_back","push_back","max_value","push_back","max_value","max_value","max_value","push_back","pop_front","max_value","push_back","max_value","max_value","max_value","pop_front","push_back","push_back","push_back","push_back","pop_front","pop_front","max_value","pop_front","pop_front","max_value","push_back","push_back","pop_front","push_back","push_back","push_back","push_back","pop_front","max_value","push_back","max_value","max_value","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","pop_front","max_value","max_value","max_value","push_back","pop_front","push_back","push_back","push_back","pop_front","max_value","pop_front","max_value","max_value","max_value","pop_front","push_back","pop_front","push_back","push_back","pop_front","push_back","pop_front","push_back","pop_front","pop_front","push_back","pop_front","pop_front","pop_front","push_back","push_back","max_value","push_back","pop_front","push_back","push_back","pop_front"],[[],[],[],[],[46],[],[],[],[],[868],[],[],[],[525],[],[],[],[],[123],[646],[],[229],[],[],[],[871],[],[],[285],[],[],[],[],[45],[140],[837],[545],[],[],[],[],[],[],[561],[237],[],[633],[98],[806],[717],[],[],[186],[],[],[],[],[],[],[268],[],[29],[],[],[],[],[866],[],[239],[3],[850],[],[],[],[],[],[],[],[310],[],[674],[770],[],[525],[],[425],[],[],[720],[],[],[],[373],[411],[],[831],[],[765],[701],[]]],
        # [],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test_obj(data_test))
        print(f'use time:{time.time() - t0}s')
​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总_卷子的博客-CSDN博客](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    