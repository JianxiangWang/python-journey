# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 9_Palindrome_Number file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        s = str(x)
        n = len(s)
        i, j = 0, n - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        s = str(x)
        n = len(s)

        if (n % 2) == 0:
            i, j = n // 2 - 1, n // 2
        else:
            i, j = n // 2, n // 2

        while i >= 0 and j < n:
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome(1))
