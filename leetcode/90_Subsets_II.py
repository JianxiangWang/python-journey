# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 90_Subsets_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nodes, comb, ans):

            ans.append(comb)

            prev = None
            for i, node in enumerate(nodes):
                if node != prev:
                    dfs(nodes[i+1:], comb + [node], ans)
                    prev = node

        nums = sorted(nums)
        ans = []
        dfs(nums, [], ans)
        return ans


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
