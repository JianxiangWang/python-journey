# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 216_Combination_Sum_III file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(nodes, comb, ans):
            if len(comb) > k:
                return
            if sum(comb) > n:
                return
            if sum(comb) == n and len(comb) == k:
                ans.append(comb)
            for i, node in enumerate(nodes):
                dfs(nodes[i + 1:], comb + [node], ans)

        ans = []
        nodes = range(1, 10)
        dfs(nodes, [], ans)
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 15))