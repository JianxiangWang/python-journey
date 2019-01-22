# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The power file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def power(self, base, exponent):
        if exponent < 0:
            return 1.0 / self._helper(base, abs(exponent))
        else:
            return self._helper(base, exponent)

    def _helper(self, base, exponent):
        if exponent == 1:
            return base
        if exponent == 0:
            return 1

        if exponent % 2 == 0:
            return self._helper(base, exponent // 2) ** 2
        else:
            return base * self._helper(base, exponent // 2) ** 2


if __name__ == '__main__':
    print(Solution().power(-2, -3))
