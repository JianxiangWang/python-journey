# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 8_String_to_Integer file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        bucket = 0
        prefix = 1
        _in = False
        for i, c in enumerate(str):
            if not _in and c == " ":
                continue
            else:
                if not _in:
                    # First Time.
                    if c == "-":
                        prefix = -1
                    elif c == "+":
                        prefix = 1
                    elif c in "0123456789":
                        bucket = 10 * bucket + int(c)
                    else:
                        return 0
                    _in = True
                else:
                    if c not in "0123456789":
                        if prefix * bucket > 2 ** 31 - 1:
                            return 2 ** 31 - 1
                        if prefix * bucket < -2 ** 31:
                            return -2 ** 31
                        return prefix * bucket
                    else:
                        bucket = 10 * bucket + int(c)

        if prefix * bucket > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if prefix * bucket < -2 ** 31:
            return -2 ** 31

        return prefix * bucket

    def myAtoi2(self, str):
        n = len(str)

        # strip.
        i = 0
        while i < n and str[i] == " ":
            i += 1

        if i == n:
            return 0

        # The first character.
        flag = 1
        if str[i] == "-":
            flag = -1
            i += 1
        if str[i] == "+":
            flag = 1
            i += 1

        # The rest number.
        ans = 0
        while i < n and str[i] in "0123456789":
            ans = ans * 10 + int(str[i])
            i += 1

        # The final result.
        ans = ans * flag
        if ans > 2 ** 31 - 1:
            ans = 2 ** 31 - 1
        if ans < -2 ** 31:
            ans = -2 ** 31

        return ans


if __name__ == '__main__':
    print(Solution().myAtoi2("4193 with words"))
