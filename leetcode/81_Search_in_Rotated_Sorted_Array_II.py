# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 81_Search_in_Rotated_Sorted_Array_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            while lo < hi and nums[lo] == nums[hi]:
                lo += 1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            else:
                if nums[lo] <= nums[mid]:
                    if nums[lo] <= target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                else:
                    if nums[mid] < target <= nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        return False
