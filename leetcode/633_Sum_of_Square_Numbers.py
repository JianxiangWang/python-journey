# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 633_Sum_of_Square_Numbers file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False

"""


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math

        i, j = 0, int(math.sqrt(c)) + 1
        while i <= j:
            x = i ** 2 + j ** 2
            if x == c:
                return True
            elif x < c:
                i += 1
            else:
                j -= 1
        return False



    def judgeSquareSum2(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0, c+1):
            for j in range(i, c+1):
                s = i**2 + j**2
                if s == c:
                    return True
                if s > c:
                    break
            if i ** 2 > c:
                break
        return False


if __name__ == '__main__':
    print(Solution().judgeSquareSum(5))