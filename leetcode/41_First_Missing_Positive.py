# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 41_First_Missing_Positive file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        [0, 1, 2, 3] ==> 0 位置放 1; 1 位置放 2，... 
        eg. 
            [3, -1, 4, 1]
            i = 0
                3 应该放在 i=2 的位置 ==》[4, -1, 3, 1]
                4 应该放在 i=3 的位置 ==》[1, -1, 3, 4]
                1 放的位置正确.
            i = 1.
        
        """

        if not nums:
            return 1
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                print(i, j)
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([4,3,2,7,8,2,3,1]))
