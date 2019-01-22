# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The rectCover file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def rectCover(self, number):
        dp = [1] * (number + 1)
        for i in range(2, number + 1):
            dp[i] = dp[i-1] + dp[i - 2]
        dp[0] = 0
        return dp[number]


if __name__ == '__main__':
    print(Solution().rectCover(2))