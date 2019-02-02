# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 121_Best_Time_to_Buy_and_Sell_Stock file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return

        n = len(prices)
        max_profit = 0
        prev_min_price = prices[0]
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - prev_min_price)
            if prices[i] < prev_min_price:
                prev_min_price = prices[i]
        return max_profit






    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_prices = []
        prev_min = None
        for i, price in enumerate(prices):
            if prev_min is None or price < prev_min:
                curr_min = price
            else:
                curr_min = prev_min
            min_prices.append(curr_min)
            prev_min = curr_min

        print(min_prices)
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - min_prices[i])

        return profit



if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4]))






























