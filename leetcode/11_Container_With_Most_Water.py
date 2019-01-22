# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 11_Container_With_Most_Water file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
"""

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        Two pointer.
        """
        ans = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            ans = max(ans, area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

    #
    # def maxArea2(self):
    #     n = len(height)
    #     ans = 0
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             s = min(height[i], height[j]) * (j - i)
    #             ans = max(ans, s)
    #
    #     return ans


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
