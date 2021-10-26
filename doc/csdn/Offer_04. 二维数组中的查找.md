### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_04. 二维数组中的查找
```



### 正文

```
### Offer_day05_04. 二维数组中的查找

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

 

限制：

0 <= n <= 1000

0 <= m <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:return False
        # 从右上角开始，如果偏小则向下，如果偏大则向左
        row_id = 0
        col_id = len(matrix[0])-1
        while row_id<len(matrix) and col_id>=0:
            num = matrix[row_id][col_id]
            if num == target:return True
            elif num>target:col_id-=1
            elif num<target:row_id+=1
        return False


def test(data_test):
    s = Solution()
    return s.findNumberIn2DArray(*data_test)


if __name__ == '__main__':
    datas = [
        [[[1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
         ],5],
        # [[[1,   4,  7, 11, 15],
        #   [2,   5,  8, 12, 19],
        #   [3,   6,  9, 16, 22],
        #   [10, 13, 14, 17, 24],
        #   [18, 21, 23, 26, 30]
        #  ],10],
        # [[[1,   4,  7, 11, 15],
        #   [2,   5,  8, 12, 19],
        #   [3,   6,  9, 16, 22],
        #   [10, 13, 14, 17, 24],
        #   [18, 21, 23, 26, 30]
        #  ],20],
        # [[],0],
        # [[[]],1],
        # [[[-1,3]],3],
        # [[[2,5],[2,8],[7,9],[7,11],[9,11]], 7],
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
    