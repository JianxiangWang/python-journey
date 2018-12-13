# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 329_Longest_Increasing_Path_in_a_Matrix file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

"""


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[None] * n for _ in range(m)]

        def dfs(x, y):
            ans = []
            for dx, dy in zip([0, 1, 0, -1], [-1, 0, 1, 0]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    if dp[nx][ny] is None:
                        dp[nx][ny] = dfs(nx, ny)
                    ans.append(dp[nx][ny])
            dp[x][y] = 1 if not ans else max(ans) + 1
            return dp[x][y]

        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    dp[i][j] = dfs(i, j)
        return max([max(x) for x in dp])

    def longestIncreasingPath_v1(self, matrix):

        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])

        def dfs(x, y, depth, ans):
            for dx, dy in zip([0, 1, 0, -1], [-1, 0, 1, 0]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    dfs(nx, ny, depth + 1, ans)
                else:
                    ans.append(depth)

        res = 0
        for i in range(m):
            for j in range(n):
                ans = []
                dfs(i, j, 1, ans)
                res = max(max(ans), res)
        return res


if __name__ == '__main__':
    nums = [[1, 2]]
    print(Solution().longestIncreasingPath(nums))
