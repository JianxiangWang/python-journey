# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The NumberOf1 file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        while n & 0xffffffff != 0:
            cnt += 1
            n = n & (n - 1)
        return cnt

    def NumberOf1_bad(self, n):
        # write code here
        cnt = 0
        while n != 0:
            if n % 2 == 1:
                cnt += 1
            n //= 2
        return cnt


if __name__ == '__main__':
    print(Solution().NumberOf1(100005))
    print(Solution().NumberOf1_bad(100005))
