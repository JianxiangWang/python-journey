# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 变态跳台阶 file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def jumpFloorII(self, number):
        dp = [1] * (number + 1)
        for i in range(1, number + 1):
            dp[i] = sum([dp[j] for j in range(i)])
        return dp[number]


if __name__ == '__main__':
    print(Solution().jumpFloorII(2))
