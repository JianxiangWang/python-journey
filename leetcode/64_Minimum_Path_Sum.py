# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 64_Minimum_Path_Sum file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        dp[i][j]: 从（0，0）到（i，j）的最小路径和
        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        """
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            dp[i][0] = sum([row[0] for row in grid][:i + 1])
        for j in range(m):
            dp[0][j] = sum(grid[0][: j + 1])

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        return dp[-1][-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(grid))
