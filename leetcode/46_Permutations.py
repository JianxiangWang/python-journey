# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 46_Permutations file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nodes, comb, res):

            if not nodes:
                res.append(comb)
                return

            for i, node in enumerate(nodes):
                dfs(nodes[:i] + nodes[i + 1:], comb + [node], res)

        res = []
        dfs(nums, [], res)
        return res


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
