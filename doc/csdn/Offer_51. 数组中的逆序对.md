### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_51. 数组中的逆序对
```



### 正文

```
### Offer_day30_51. 数组中的逆序对

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
from leetcode_python.utils import *

class Solution:
    def __init__(self):
        self.res = 0

    def merge(self, left_list: List[int], right_list: List[int]) -> List[int]:
        res_merge = []
        left_length, right_length = len(left_list), len(right_list)
        left_index, right_index = 0, 0
        while left_index < left_length and right_index < right_length:
            if left_list[left_index] <= right_list[right_index]:
                res_merge.append(left_list[left_index])
                left_index += 1
            else:
                res_merge.append(right_list[right_index])
                right_index += 1
                self.res += left_length-left_index
        if left_index < left_length:
            res_merge.extend(left_list[left_index:])
        if right_index < right_length:
            res_merge.extend(right_list[right_index:])
        return res_merge

    def merge_sort(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length<=1:return nums
        mid = length//2
        left_list = self.merge_sort(nums[:mid])
        right_list = self.merge_sort(nums[mid:])
        res_sort = self.merge(left_list,right_list)
        return res_sort

    def reversePairs(self, nums: List[int]) -> int:
        self.merge_sort(nums)
        return self.res

def test(data_test):
    s = Solution()
    return s.reversePairs(data_test)


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
        [7,5,6,4],
    ]
    # datas = [[814, 261, 334, 178, 574, 102, 285, 492, 272, 577, 526, 412, 273, 355, 125, 460, 414, 300, 619, 342], [403, 787, 65, 629, 603, 701, 831, 24, 516, 91, 137, 699, 24, 362, 222, 569, 317, 70, 887, 620], [720, 477, 421, 169, 787, 696, 413, 708, 556, 261, 170, 529, 179, 165, 558, 462, 494, 237, 860, 46], [489, 305, 689, 723, 284, 550, 112, 707, 645, 771, 427, 493, 301, 41, 554, 765, 700, 428, 666, 834], [186, 354, 419, 445, 161, 312, 192, 852, 546, 655, 888, 685, 714, 446, 44, 33, 762, 427, 34, 172], [665, 794, 562, 340, 708, 247, 251, 289, 232, 877, 371, 595, 360, 285, 669, 363, 562, 273, 730, 538], [362, 301, 441, 294, 478, 525, 523, 697, 515, 743, 564, 774, 170, 516, 510, 498, 349, 241, 93, 280], [564, 637, 777, 279, 709, 693, 311, 585, 127, 506, 662, 770, 422, 711, 412, 469, 172, 246, 316, 578], [57, 543, 798, 353, 687, 751, 494, 873, 830, 230, 58, 272, 838, 550, 802, 76, 332, 805, 797, 727], [728, 47, 456, 387, 227, 806, 232, 817, 827, 351, 346, 630, 52, 816, 706, 424, 462, 766, 781, 334]]

    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
    # print(randListListInt(1,888,20,10))
    # randListListIntShow(1,1888,49999,10)
​```

备注：
GitHub：[https://github.com/monijuan/leetcode_python ](https://github.com/monijuan/leetcode_python)

CSDN汇总：[模拟卷Leetcode 题解汇总_卷子的博客-CSDN博客](https://blog.csdn.net/qq_34451909/article/details/120968335)

可以加QQ群交流：==*1092754609*==

> leetcode_python.utils详见汇总页说明
> 先刷的题，之后用脚本生成的blog，如果有错请留言，我看到了会修改的！谢谢！

```
    