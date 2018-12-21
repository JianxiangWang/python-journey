# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 63_Unique_Paths_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i][0] = 1 if obstacleGrid[i][0] == 0 else 0
            else:
                dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        for j in range(m):
            if j == 0:
                dp[0][j] = 1 if obstacleGrid[0][j] == 0 else 0
            else:
                dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    x = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(Solution().uniquePathsWithObstacles(x))
