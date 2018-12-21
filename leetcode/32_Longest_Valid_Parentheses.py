# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 32_Longest_Valid_Parentheses file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""


class Solution:

    def longestValidParentheses(self, s):
        """
        1. '...()()'
            dp[i] = dp[i-2] + 2
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n <= 1:
            return 0
        dp = [0] * len(s)
        for i in range(n):
            # 1. '...()()' : dp[i] = dp[i-2] + 2
            if s[i] == ")":
                if i - 1< 0:
                    continue

                if s[i-1] == "(":
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                # 2. '..)()(())'
                if s[i-1] == ")":
                    if i - dp[i-1] - 1 >=0 and s[i - dp[i-1] - 1] == "(":
                        if i - dp[i-1] - 2 >= 0:
                            dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                        else:
                            dp[i] = dp[i - 1] + 2

        return max(dp)

    def longestValidParentheses_stack(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Using stack.
        ans = 0
        stack = []
        for x in s:
            if not stack:
                stack.append(x)
                continue

            o = stack[-1]
            if o == "(" and x == ")":
                stack.pop()
                ans += 1
            elif o == ")" and x == "(":
                stack.pop()
                ans += 1
            else:
                stack.append(x)

        return ans * 2


if __name__ == '__main__':
    print(Solution().longestValidParentheses(")("))
