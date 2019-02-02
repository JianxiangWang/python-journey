# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 5_longest_palindromic_substring file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:

    def longestPalindrome_brute_force(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        def is_palindrome(string):
            i, j = 0, len(string) - 1
            while i <= j:
                if string[i] == string[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        n = len(s)
        ans = ""
        for i in range(n):
            for j in range(i, n):
                sub_string = s[i: j + 1]
                if is_palindrome(sub_string):
                    if not ans or (len(sub_string) > len(ans)):
                        ans = sub_string
        return ans

    def longestPalindrome_DP(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        1. j - i <= 1:
            if s[i] == s[j]: dp[i][j] = True
            
        2. j - i > 1:
            dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False. 
        
        """

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        for i in range(n)[::-1]:
            for j in range(i, n):
                if j - i <= 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        if not ans or (j - i + 1) > len(ans):
                            ans = s[i: j + 1]
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        if not ans or (j - i + 1) > len(ans):
                            ans = s[i: j + 1]
        return ans

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0 or n == 1:
            return s
        ans = s[0]
        for i in range(n):
            for j in range(i + 1, n):
                sub_str = s[i: j + 1]
                if self._is_palindrome(sub_str):
                    if ans is None or len(sub_str) > len(ans):
                        ans = sub_str
        return ans

    def _is_palindrome(self, s):
        n = len(s)
        if n % 2 == 0:
            if s[: n // 2] == s[n // 2:][::-1]:
                return True
            else:
                return False
        else:
            if s[: n // 2] == s[n // 2 + 1:][::-1]:
                return True
            else:
                return False

    def longestPalindrome2(self, s):
        """
        O(n^2), Expand Around Center
        """
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            l1 = self._expand_around_center(s, i, i)
            l2 = self._expand_around_center(s, i, i + 1)
            l = max(l1, l2)
            if l > (end - start):
                start = i - (l - 1) // 2
                end = i + (l) // 2 + 1
        return s[start: end]

    def _expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == '__main__':
    print(Solution().longestPalindrome_DP("bdweaadb"))
