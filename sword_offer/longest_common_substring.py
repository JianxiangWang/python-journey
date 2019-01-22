# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The longest_common_substring file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
import itertools


def longest_common_substring(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0

    return max(itertools.chain(*dp))


if __name__ == '__main__':
    print(longest_common_substring("asasbcas", "xxbcXX"))