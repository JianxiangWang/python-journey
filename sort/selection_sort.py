# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The selection_sort file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution(object):
    def selection_sort(self, nums):
        """
        :type nums: list
        """
        n = len(nums)
        for i in range(n-1):
            min_j = i
            for j in range(i, n):
                if nums[j] < nums[min_j]:
                    min_j = j
            nums[i], nums[min_j] = nums[min_j], nums[i]


if __name__ == '__main__':
    nums = [0, -1, 12, 9, 4]
    Solution().selection_sort(nums)
    print(nums)