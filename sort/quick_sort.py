# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The quick_sort file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution(object):

    def quick_sort(self, nums, lo, hi):
        if lo < hi:
            pi = self.partition(nums, lo, hi)
            self.quick_sort(nums, lo, pi - 1)
            self.quick_sort(nums, pi + 1, hi)

    def partition(self, nums, lo, hi):
        """
        i和j的值不断的靠拢，然后最终停止，结束一次排序
        """
        if lo >= hi:
            return
        pivot = nums[lo]
        i, j = lo, hi
        while i < j:
            # 和最右边的比较，如果>=pivot,然后j-1，慢慢的和前一个值比较; 如果值<key，那么就交换位置
            while i < j and nums[j] >= pivot:
                j -= 1
            nums[i] = nums[j]
            # 交换位置后，然后在和最左边的值开始比较，如果<=pivot,然后i+1，慢慢的和后一个值比较;如果值>pivot，那么就交换位置
            while i < j and nums[i] <= pivot:
                i += 1
            nums[j] = nums[i]

        nums[i] = pivot
        return i


if __name__ == '__main__':
    nums = [4, 1, 2, 3, -9, 123, 126]
    Solution().quick_sort(nums, 0, len(nums) - 1)
    print(nums)
