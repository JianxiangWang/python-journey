# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 78_Subsets file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nodes, comb, ans):
            ans.append(comb)
            for i, node in enumerate(nodes):
                dfs(nodes[i + 1:], comb + [node], ans)

        ans = []
        dfs(nums, [], ans)
        return ans


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))