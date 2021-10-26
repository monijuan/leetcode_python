### 标题

```
模拟卷Leetcode【剑指 Offer】剑指 Offer II 069. 山峰数组的顶部
```



### 正文

```
### 剑指 Offer II 069. 山峰数组的顶部

符合下列属性的数组 arr 称为 山峰数组（山脉数组） ：

arr.length >= 3
存在 i（0 < i < arr.length - 1）使得：
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
给定由整数组成的山峰数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i ，即山峰顶部。

 

示例 1：

输入：arr = [0,1,0]
输出：1
示例 2：

输入：arr = [1,3,5,4,2]
输出：2
示例 3：

输入：arr = [0,10,5,2]
输出：1
示例 4：

输入：arr = [3,4,5,1]
输出：2
示例 5：

输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
 

提示：

3 <= arr.length <= 104
0 <= arr[i] <= 106
题目数据保证 arr 是一个山脉数组
 

进阶：很容易想到时间复杂度 O(n) 的解决方案，你可以设计一个 O(log(n)) 的解决方案吗？

 

注意：本题与主站 852 题相同：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/B1IidL
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
from leetcode_python.utils import *


class Solution:
    def __init__(self):
        pass

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,mid,right = 0,len(arr)//2,len(arr)
        num_mid = arr[mid]
        while not (arr[mid-1]<num_mid>arr[mid+1]):
            if arr[mid-1]<num_mid:left = mid
            elif num_mid>arr[mid+1]:right=mid
            mid = left + (right-left)//2
            num_mid = arr[mid]
        return mid

    def peakIndexInMountainArray__(self, arr: List[int]) -> int:
        left,mid,right = 0,len(arr)//2,len(arr)
        num_left,num_mid,num_right = arr[0],arr[mid],arr[-1]
        while not (arr[mid-1]<num_mid>arr[mid+1]):
            if arr[mid-1]<num_mid>arr[mid+1]:return mid
            elif arr[mid-1]<num_mid:
                left,num_left = mid,num_mid
            elif num_mid>arr[mid+1]:
                right,num_right = mid,num_mid
            mid = left + (right-left)//2
            num_mid = arr[mid]
        return mid


def test(data_test):
    s = Solution()
    return s.peakIndexInMountainArray(*data_test)


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
        [[40,48,61,75,100,99,98,39,30,10]],
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
    