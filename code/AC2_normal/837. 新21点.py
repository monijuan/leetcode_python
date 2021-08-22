# -*- coding: utf-8 -*-
# @Time    : 2021/8/16 16:46
# @Author  : xxxxxxxxx
# @Email   : xxxxxxxxxxx@xxx.com
# @File    : 837. 新21点.py
# @Software: PyCharm
# ===================================
"""爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：

爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

 

示例 1：

输入：N = 10, K = 1, W = 10
输出：1.00000
说明：爱丽丝得到一张卡，然后停止。
示例 2：

输入：N = 6, K = 1, W = 10
输出：0.60000
说明：爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
示例 3：

输入：N = 21, K = 17, W = 10
输出：0.73278
 

提示：

0 <= K <= N <= 10000
1 <= W <= 10000
如果答案与正确答案的误差不超过 10^-5，则该答案将被视为正确答案通过。
此问题的判断限制时间已经减少。

"""
import time
from typing import List


class Solution:
    def __init__(self):
        pass

    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        """
        :param n: 求 <=n 的概率
        :param k: 当 >=k 时停止
        :param maxPts:  最大数
        :return:  <=n 的概率
        """
        last = k+maxPts
        factor = 1./maxPts
        dp = [0 for _ in range(last+1)]
        dp[0] = 1
        dp[1] = factor
        if k==0 :return 1
        elif k==1 :return min(1.,n/maxPts)
        for index in range(2,last):
            if index<=k and index<=maxPts:
                dp[index] = dp[index-1] + factor * dp[index-1]
            elif index<=k and index>maxPts:
                dp[index] = dp[index-1] + factor * (dp[index-1] - dp[index - maxPts-1])
            else:
                dp[index] = dp[index-1] - factor * dp[index-maxPts-1]
        return sum(dp[k:n+1])

    def new21Game动态规划超时优化(self, n: int, k: int, maxPts: int) -> float:
        last = k+maxPts
        factor = 1./maxPts
        dp = [0 for i in range(last+1)]
        dp[0] = 1.
        if k==0 :return 1
        elif k==1 :return min(1.,n/maxPts)
        for index in range(1,last):
            dp[index] = factor * (sum(dp[max(1, index-maxPts):min(index,k)]))
            if index <= maxPts:  dp[index] += factor
        # print(dp)
        return sum(dp[k:n+1])

    def new21Game动态规划超时(self, n: int, k: int, maxPts: int) -> float:
        last = k+maxPts
        factor = 1./maxPts
        dp = [0 for i in range(last+1)]
        dp[0] = 1.
        for index in range(1,last):
            if index < k:    # 没有停止，由前面 maxPts 个数得出
                if index<=maxPts:   # 前面还没有 maxPts 个数，需要加上第一次的概率 factor
                    dp[index] = factor + factor * sum(dp[1:index])
                else:
                    dp[index] = factor * (sum(dp[max(1,index-maxPts):index]))
                    # dp[index-maxPts]=0
            else:  # 停止，由前面 maxPts 个数中，小于 k 的数得出
                if index<=maxPts and k>0: # 前面还没有 maxPts 个数，需要加上第一次的概率 factor
                    dp[index] = factor + factor * sum(dp[1:k])
                else:
                    dp[index] = factor * (sum(dp[max(1, index-maxPts):k]))
                    # dp[index-maxPts]=0
            # if index>=maxPts:dp[index-maxPts]=0
            print('i=',index,[round(x,3) for x in dp])
        # print(dp)
        return sum(dp[k:n+1])

    def new21Game暴力求解(self, n: int, k: int, maxPts: int) -> float:
        prob_factors=[0 for _ in range(k+1)]
        # global prob
        def getCard(score,prob_factor):
            # global prob
            if score<k: # 继续抽卡
                for next_card in range(1,maxPts+1):
                    getCard(score + next_card, prob_factor+1)
            elif score<=n: # 停止抽卡，并且计算概率
                prob_factors[prob_factor]+=1
                # prob += 1./maxPts**prob_factor
        getCard(0,0)

        prob = 0
        for index,times in enumerate(prob_factors):
            prob+=times * 1/maxPts**index

        # print(prob_factors)
        return prob

def test(data_test):
    s = Solution()
    # return s.new21Game暴力求解(*data_test)
    return s.new21Game动态规划超时(*data_test)
    # return s.new21Game动态规划超时优化(*data_test)
    return s.new21Game(*data_test)


if __name__ == '__main__':
    datas = [
        # [10, 1, 10],
        # [10, 2, 10],
        # [4, 3, 10],
        # [5, 3, 10],
        # [6, 3, 10],
        # [11, 3, 10],
        # [12, 3, 10],
        # [6, 1, 10],
        # [6, 2, 10],
        [21, 17, 10],   # 0.7327777870686083
        # # [11, 7, 10],
        # [0, 0, 1],      # 1
        # [1, 0, 1],      # 1
        # [1, 0, 2],      # 1
        # [121, 100, 47],
        # [421, 400, 47],     # 0.7118794328537366
        # [9811, 8890, 7719], # 0.20910837511099467
        # [3, 2, 3], # 0.8888888888888888
        # [12, 1, 10], # 1.0
    ]
    for data_test in datas:
        t0 = time.time()
        print('-'*50)
        print('input:', data_test)
        print('output:', test(data_test))
        print(f'use time:{time.time() - t0}s')
