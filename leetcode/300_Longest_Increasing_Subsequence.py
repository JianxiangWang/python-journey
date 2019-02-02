# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 300_Longest_Increasing_Subsequence file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

"""


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        dp[i]: 表示以i结尾的最长子序列的长度
        dp[i] 可以从 dp[i-1] (if s[i] > s[i-1]), dp[i-2] (if s[i] > s[i-2]), dp[i-3], ... dp[0] 跳转过来，选择最大的那一个
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            options = [dp[j] + 1 for j in range(i) if nums[i] > nums[j]]
            dp[i] = max(options) if options else 1
        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))




