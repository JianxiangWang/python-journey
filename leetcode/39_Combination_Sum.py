# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 39_Combination_Sum file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(nodes, comb, ans):
            if not nodes:
                return
            if sum(comb) == target:
                ans.append(comb)
            if sum(comb) > target:
                return
            for i, node in enumerate(nodes):
                dfs(nodes[i:], comb + [node], ans)

        ans = []
        dfs(candidates, [], ans)
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 5], 8))
