# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 123_Best_Time_to_Buy_and_Sell_Stock_III file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
import math


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        s1, s2, s3, s4 = -prices[0], -math.inf, -math.inf, -math.inf
        for i, price in enumerate(prices):
            s1 = max(s1, -price)
            s2 = max(s2, s1 + price)
            s3 = max(s3, s2 - price)
            s4 = max(s4, s3 + price)

        return max(0, s4)


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        # dp1[i] 表示从 0-i, 包含i的最大利润
        dp1 = [None] * len(prices)
        dp1[0] = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i - 1], prices[i] - min_price)
            if prices[i] < min_price:
                min_price = prices[i]

        # dp2[i] 表示 i 到 N 的最大利润
        # 反向遍历, dp[i] = max(dp[i+1], prices[i] - max_price)
        dp2 = [None] * len(prices)
        dp2[-1] = 0
        max_price = prices[-1]
        for i in range(0, len(prices) - 1)[::-1]:
            dp2[i] = max(dp2[i + 1], max_price - prices[i])
            if prices[i] > max_price:
                max_price = prices[i]

        # 有了dp1, dp2, 遍历所有的划分, 获取最大profit
        max_profit = 0
        for i in range(len(prices)):
            profit_1 = dp1[i]
            if i + 1 > len(prices) - 1:
                profit_2 = 0
            else:
                profit_2 = dp2[i + 1]

            if profit_1 + profit_2 > max_profit:
                max_profit = profit_1 + profit_2

        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
