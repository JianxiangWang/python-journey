# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 10_Regular_Expression_Matching file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = text and (text[0] == pattern[0] or pattern[0] == ".")

        if len(pattern) >= 2 and pattern[1] == "*":
            return self.isMatch(text, pattern[2:]) or (first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == '__main__':
    print(Solution().isMatch("ab", "a."))
