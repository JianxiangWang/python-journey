# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 40_Combination_Sum_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(nodes, comb, ans):
            if sum(comb) == target:
                ans.append(comb)
            if sum(comb) > target:
                return
            prev_node = None
            for i, node in enumerate(nodes):
                if node != prev_node:
                    dfs(nodes[i + 1:], comb + [node], ans)
                    prev_node = node
        ans = []
        candidates = sorted(candidates)
        dfs(candidates, [], ans)
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
