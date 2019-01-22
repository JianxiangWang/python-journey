# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 15_3Sum file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        n = len(nums)
        prev = None
        for i in range(n - 2):
            if prev == nums[i]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                sum0 = nums[i] + nums[l] + nums[r]
                if sum0 == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif sum0 > 0:
                    r -= 1
                else:
                    l += 1
            prev = nums[i]
        return ans


if __name__ == '__main__':
    print(Solution().threeSum([-2,0,0,2,2]))
