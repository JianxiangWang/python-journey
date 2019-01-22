# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The bubble_sort file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution(object):
    def bubble_sort(self, nums):
        """
        :type nums: list
        """
        n = len(nums)
        for j in range(n, 0, -1):
            for i in range(j - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]


if __name__ == '__main__':
    nums = []
    Solution().bubble_sort(nums)
    print(nums)
