### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_28. 对称的二叉树
```



### 正文

```
### Offer_day07_28. 对称的二叉树

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

​```cpp
    1
   / \
  2   2
 / \ / \
3  4 4  3
​```

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

​```cpp
    1
   / \
  2   2
   \   \
   3    3
​```

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
 

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




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

    def isSameRoot(self, leftson,rightson) -> bool:
        if leftson and rightson:
            if leftson.val==rightson.val:
                return self.isSameRoot(leftson.left,rightson.right) and self.isSameRoot(leftson.right,rightson.left)
            else:
                return False
        elif not leftson and not rightson:
            return True
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.isSameRoot(root.left,root.right)
        else:
            return True


def test(data_test):
    s = Solution()
    return s.isSymmetric(*data_test)


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
