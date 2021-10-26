### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_26. 树的子结构
```



### 正文

```
### Offer_day07_26. 树的子结构






代码：

​```python
import time
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        pass

    def isSame(self, A: TreeNode, B: TreeNode) -> bool:
        if A is not None and B is not None:
            if B.val==A.val:
                return self.isSame(A.left,B.left) and self.isSame(A.right,B.right)
            else:
                return False
        elif B is None:
            return True
        else:
            return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:return False
        queue = [A]
        while len(queue):
            head = queue.pop(0)
            if head:
                if self.isSame(head,B):return True
                queue.append(head.left)
                queue.append(head.right)
        return False

class Solution_官方:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


def test(data_test):
    s = Solution()
    return s.isSubStructure(*data_test)


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
​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总_卷子的博客-CSDN博客](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    