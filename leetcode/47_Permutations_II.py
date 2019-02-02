# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 47_Permutations_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nodes, comb, ans):
            if not nodes:
                ans.append(comb)
                return

            prev = None
            for i, node in enumerate(nodes):
                if node != prev:
                    dfs(nodes[:i] + nodes[i+1:], comb + [node], ans)
                    prev = node
        ans = []
        nums = sorted(nums)
        dfs(nums, [], ans)
        return ans

    def permuteUnique_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nodes, comb, res):

            if not nodes:
                res.append(comb)
                return

            for i, node in enumerate(set(nodes)):
                next_nodes = []
                first_time = True
                for x in nodes:
                    if x == node and first_time:
                        first_time = False
                        continue
                    next_nodes.append(x)
                dfs(next_nodes, comb + [node], res)

        res = []
        dfs(nums, [], res)
        return res


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
