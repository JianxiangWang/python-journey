# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The insert_sort file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution(object):
    def insert_sort(self, nums):
        """
        :type nums: list
        """
        n = len(nums)
        for j in range(1, n):
            for i in range(j, 0, -1):
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
                else:
                    break


if __name__ == '__main__':
    nums = []
    Solution().insert_sort(nums=nums)
    print(nums)