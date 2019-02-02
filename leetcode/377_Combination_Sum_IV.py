# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 377_Combination_Sum_IV file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""



class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                dp[i] += 0 if i - num < 0 else dp[i - num]
        return dp[-1]


    def combinationSum4DFS(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def dfs(nodes, comb, ans):
            if sum(comb) > target:
                return
            if sum(comb) == target:
                ans.append(comb)
                return
            for i, node in enumerate(nodes):
                dfs(nodes, comb + [node], ans)

        ans = []
        dfs(nums, [], ans)
        return len(ans)


if __name__ == '__main__':
    print(Solution().combinationSum4([3, 2, 1], 4))
