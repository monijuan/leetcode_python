# -*- coding: utf-8 -*-
# @Time    : 2022/5/8 10:26
# @Author  : 模拟卷
# @Github  : https://github.com/monijuan
# @CSDN    : https://blog.csdn.net/qq_34451909
# @File    : 6058AC. 统计打字方案数.py
# @Software: PyCharm 
# ===================================
"""Alice 在给 Bob 用手机打字。数字到字母的 对应 如下图所示。



为了 打出 一个字母，Alice 需要 按 对应字母 i 次，i 是该字母在这个按键上所处的位置。

比方说，为了按出字母 's' ，Alice 需要按 '7' 四次。类似的， Alice 需要按 '5' 两次得到字母  'k' 。
注意，数字 '0' 和 '1' 不映射到任何字母，所以 Alice 不 使用它们。
但是，由于传输的错误，Bob 没有收到 Alice 打字的字母信息，反而收到了 按键的字符串信息 。

比方说，Alice 发出的信息为 "bob" ，Bob 将收到字符串 "2266622" 。
给你一个字符串 pressedKeys ，表示 Bob 收到的字符串，请你返回 Alice 总共可能发出多少种文字信息 。

由于答案可能很大，将它对 109 + 7 取余 后返回。



示例 1：

输入：pressedKeys = "22233"
输出：8
解释：
Alice 可能发出的文字信息包括：
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae" 和 "ce" 。
由于总共有 8 种可能的信息，所以我们返回 8 。
示例 2：

输入：pressedKeys = "222222222222222222222222222222222222"
输出：82876089
解释：
总共有 2082876103 种 Alice 可能发出的文字信息。
由于我们需要将答案对 109 + 7 取余，所以我们返回 2082876103 % (109 + 7) = 82876089 。


提示：

1 <= pressedKeys.length <= 105
pressedKeys 只包含数字 '2' 到 '9' 。
"""
from leetcode_python.utils import *

MOD = 10 ** 9 + 7


@lru_cache(None)
def base3(length):
    if length < 4:
        return [0, 1, 2, 4][length]
    dp = [[0] * (length + 1) for _ in range(5)]
    dp[4][0] = 1
    for i in range(1, length + 1):
        # print(i,dp)
        dp[1][i] = dp[4][i - 1]
        if i > 1:
            dp[2][i] = dp[4][i - 2]
        if i > 2:
            dp[3][i] = dp[4][i - 3]
        dp[4][i] = dp[1][i] + dp[2][i] + dp[3][i]
        # print(i)
        # for l in dp:
        #     print(f' {l}')
    return dp[-1][-1]


@lru_cache(None)
def base4(length):
    if length < 4:
        return [0, 1, 2, 4][length]
    dp = [[0] * (length + 1) for _ in range(6)]
    dp[5][0] = 1
    for i in range(1, length + 1):
        dp[1][i] = dp[5][i - 1]
        if i > 1:
            dp[2][i] = dp[5][i - 2]
        if i > 2:
            dp[3][i] = dp[5][i - 3]
        if i > 3:
            dp[4][i] = dp[5][i - 4]
        dp[5][i] = dp[1][i] + dp[2][i] + dp[3][i] + dp[4][i]
        # print(i)
        # for l in dp:
        #     print(f' {l}')
    return dp[-1][-1]


class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        l = len(pressedKeys)
        i = 0
        res = 1
        while i < l:
            j = i
            while j < l and pressedKeys[j] == pressedKeys[i]:
                j += 1
            c = pressedKeys[i]
            length = j - i
            if c in '79':
                r = base4(length)
            else:
                r = base3(length)
            res *= r
            res %= MOD
            i = j
        return res


def test(data_test):
    s = Solution()
    data = data_test  # normal
    # data = [List2Node(data_test[0])]  # list转node
    return s.countTexts(*data)


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
        # ["777777"],
        # ["222222222222222222222222222222222222"],
        ["355577777788899"],
    ]
    for data_test in datas:
        t0 = time.time()
        print('-' * 50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
