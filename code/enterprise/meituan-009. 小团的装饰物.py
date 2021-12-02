# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 10:34
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : meituan-009. 小团的装饰物.py
# @Software: PyCharm
# ===================================
"""小团正在装饰自己的书桌，他的书桌上从左到右有 m 个空位需要放上装饰物。商店中每个整数价格的装饰物恰好有一种，且每种装饰物的数量无限多。
小团去商店的时候，想到了一个购买方案，他要让右边的装饰物价格是左边的倍数。用数学语言来说，假设小团的 m 个装饰物价格为 a[1], a[2], ..., a[m] ，那么对于任意的 1≤i≤j≤m ，a[j] 是 a[i] 的倍数。
小团是一个节约的人，他希望最贵的装饰物不超过 n 元。现在，请你计算小团有多少种购买的方案？

格式：


输入：
- 输入包含两个数，n 和 m 。
输出：
- 输出一个数，结果对 998244353 取模，表示购买的方案数。
示例：


输入：4 2
输出：8
解释：[1,1][1,2][1,3][1,4][2,2][2,4][3,3][4,4] 共 8 种。
提示：

对于 40% 的数据，n, m ≤ 10
对于 100% 的数据，1 ≤ n, m ≤ 1000
请注意，本题需要自行编写「标准输入」和「标准输出」逻辑，以及自行 import/include 需要的 library。了解书写规则

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/0VvYxa
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

money,num = 123,645

def 超时():
    MOD = 998244353
    money,num = list(map(int,input().split()))
    cnt_last_price = [0]+[1]*money # 对于左边物品  cnt[价格]=可选择总数
    for _ in range(num-1):
        cnt_now_price = [0]*(money+1) #
        for last_pri in range(1, money + 1):# 倍数，最多可能是money倍
            for pri in range(last_pri, money + 1, last_pri):
                cnt_now_price[pri] = (cnt_now_price[pri] + cnt_last_price[last_pri]) % MOD
        cnt_last_price = cnt_now_price
    print(sum(cnt_now_price) % MOD)



