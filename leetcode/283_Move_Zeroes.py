# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 283_Move_Zeroes file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, n):
            nums[i] = 0


    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[i] != 0:
                i += 1
            while i <= j and nums[j] == 0:
                j -= 1
            if i > j:
                break
            for k in range(i, j):
                nums[k] = nums[k+1]
            nums[j] = 0
            j -= 1

if __name__ == '__main__':
    x = [0, 0, 1]
    Solution().moveZeroes(x)
    print(x)