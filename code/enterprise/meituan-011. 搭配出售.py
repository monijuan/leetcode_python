# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 10:12
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-011. 搭配出售.py
# @Software: PyCharm
# ===================================
"""服装店新进了 a 条领带，b 条裤子，c 个帽子，d 件衬衫，现在要把这些搭配起来售卖。有三种搭配方式，一条领带和一件衬衫，一条裤子和一件衬衫，一个帽子和一件衬衫。卖出一套领带加衬衫可以得到 e 元，卖出一套裤子加衬衫可以得到 f 元，卖出一套帽子加衬衫可以得到 g 元。现在你需要输出最大获利。

格式：


输入：
- 一行 7 个整数分别表示 a, b, c, d, e, f, g 。
输出：
- 最大获利。
示例：


输入：2 3 4 5 6 7 8
输出：39
解释：4 个帽子加 4 件衬衫获利 32 元，1 条裤子加 1 件衬衫获利 7 元，一共得到 39 元。
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/0JzXQB
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

nums = list(map(int,input().split()))
sortid = sorted(enumerate(nums[-3:]),key= lambda pair:-pair[1])
res = 0
for id,pri in sortid:
    num_sell = min(nums[3],nums[id])
    res += num_sell*pri
    nums[3] -= num_sell
print(res)
