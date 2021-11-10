### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_33. 二叉搜索树的后序遍历序列
```



### 正文

```
### Offer_day20_33. 二叉搜索树的后序遍历序列

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def verifyPostorder(self, postorder: List[int]) -> bool:
        length = len(postorder)
        if length<3:return True
        last = postorder[-1]
        first_bigger_id = 0
        # while postorder[first_bigger_id]<last and first_bigger_id<length:
        while postorder[first_bigger_id]<last:
            first_bigger_id+=1
        if len(postorder[first_bigger_id:-1]) and min(postorder[first_bigger_id:-1])<last:
            return False
        else:
            return self.verifyPostorder(postorder[:first_bigger_id]) and self.verifyPostorder(postorder[first_bigger_id:-1])


def test(data_test):
    s = Solution()
    return s.verifyPostorder(*data_test)


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
        [[4, 8, 6, 12, 16, 14, 10]],
        [[1,2,5,10,6,9,4,3]],
        [[1,6,3,2,5]],
        [[1,3,2,6,5]],
        [[1, 2, 3, 4, 5]],
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
    