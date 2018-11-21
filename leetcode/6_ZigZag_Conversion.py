# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 6_ZigZag_Conversion file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        i, step = 0, 1
        for c in s:
            print(ans)
            ans[i].append(c)
            if i == numRows - 1:
                step = -1
            if i == 0:
                step = 1
            i += step

        res = "".join(["".join(x) for x in ans])
        return res


if __name__ == '__main__':
    print(Solution().convert("AB", numRows=2))


