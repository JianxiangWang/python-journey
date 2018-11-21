# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 7_reverse_integer file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10

        return res if res <= 0x7fffffff else 0


if __name__ == '__main__':
    print(Solution().reverse(-123000))


