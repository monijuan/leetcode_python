### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_13. 机器人的运动范围
```



### 正文

```
### Offer_day14_13. 机器人的运动范围

地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
提示：

1 <= n,m <= 100
0 <= k <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def movingCount(self, m: int, n: int, k: int) -> int:
        res = 0
        arrived_last_row = [False for _ in range(m)]
        for row_id in range(m):
            arrived_this_row = [False for _ in range(n)]
            sum_a = sum([int(x) for x in str(row_id)])
            for col_id in range(n):
                arrived_left = False if col_id==0 else arrived_this_row[col_id-1]
                arrived_up = False if row_id==0 else arrived_last_row[col_id]
                if arrived_left or arrived_up or (0==row_id and 0==col_id):
                    sum_b = sum([int(x) for x in str(col_id)])
                    if sum_a+sum_b<=k:
                        res+=1
                        arrived_this_row[col_id] = True
                    else:
                        arrived_this_row[col_id] = False
            arrived_last_row = arrived_this_row
            # print(arrived_last_row)
        return res

    def movingCount_穿墙错误(self, m: int, n: int, k: int) -> int:
        res = 0
        for a in range(m):
            sum_a = sum([int(x) for x in str(a)])
            for b in range(n):
                sum_b = sum([int(x) for x in str(b)])
                if sum_a+sum_b<=k:
                    res+=1
        return res


def test(data_test):
    s = Solution()
    return s.movingCount(*data_test)


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
        # [1,2,1],
        # [3,2,17],
        # [2,3,1],
        # [3,1,0],
        [20,20,10],
        # [100,100,20],
        # [100,100,10],
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
    