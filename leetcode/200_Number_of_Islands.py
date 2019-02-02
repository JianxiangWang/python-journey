# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 200_Number_of_Islands file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(i, j):
            if grid[i][j] == '1' and not visited[i][j]:
                visited[i][j] = True
            else:
                return
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                next_i, next_j = i + dx, j + dy
                if next_i < 0 or next_i >= n:
                    continue
                if next_j < 0 or next_j >= m:
                    continue
                dfs(next_i, next_j)

        num_islands = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                if grid[i][j] == '0':
                    visited[i][j] = True
                    continue
                # For the value of 1.
                num_islands += 1
                dfs(i, j)

        return num_islands


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    print(Solution().numIslands(grid))
