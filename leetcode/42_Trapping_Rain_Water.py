# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 42_Trapping_Rain_Water file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""


class Solution:
    def trap(self, height):
        """
        对于A[i],如果A[i]这个位置可以装水，那么左右两边必定各有一个数大于A[i],
        （设为left[i]和right[i]）且这个位置能放的量最多为min(left[i],right[i]) – A[i]
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        for i in range(1, n):
            left_max[i] = max(height[i - 1], left_max[i - 1])
        for j in range(n - 2, -1, -1):
            right_max[j] = max(height[j + 1], right_max[j + 1])
        ans = 0
        for k, h in enumerate(height):
            l, r = left_max[k], right_max[k]
            if l > h and r > h:
                ans += min(l, r) - h
        return ans


if __name__ == '__main__':
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
