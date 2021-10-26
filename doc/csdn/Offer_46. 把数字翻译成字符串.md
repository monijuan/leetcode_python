### 标题

```
模拟卷Leetcode【剑指 Offer】Offer_46. 把数字翻译成字符串
```



### 正文

```
### Offer_day10_46. 把数字翻译成字符串

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




代码：

​```python
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def translateNum(self, num: int) -> int:
        chars = list(str(num))
        dp = [0 for _ in range(len(chars)+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(chars)+1):
            ab = int(chars[i-2]+chars[i-1])
            if 10<=ab<=25:
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        return dp[-1]

    def translateNum22(self, num: int) -> int:
        chars = list(str(num))
        dp = [0 for _ in range(len(chars)+1)]
        dp[-1] = 0
        dp[-2] = 1
        cnt = 1
        for i in range(len(chars)-2,-1,-1):
            ab = int(chars[i]+chars[i+1])
            if 10<=ab<=25:
                # dp[i]=max(dp[i+1],dp[i+2]+1)
                # dp[i]=dp[i+1]+1
                dp[i]=dp[i+2]*2
                cnt+=1
            else:
                dp[i]=dp[i+1]
            print(dp,cnt)
        return cnt


def test(data_test):
    s = Solution()
    return s.translateNum(*data_test)


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
        # [12258],
        # [0],
        # [00],
        # [25],
        [113011],
        # [12100322],
        # [12031020],
        # [15354],
        # [120034],
        # [12132131],
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
    