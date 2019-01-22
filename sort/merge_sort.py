# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The merge_sort file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution(object):
    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        left, right = nums[:n // 2], nums[n // 2:]
        left_ = self.merge_sort(left)
        right_ = self.merge_sort(right)

        return self._merge(left_, right_)

    def _merge(self, left, right):
        m, n = len(left), len(right)
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[i])
                j += 1

        while i < m:
            res.append(left[i])
            i += 1

        while j < n:
            res.append(right[j])
            j += 1

        return res


if __name__ == '__main__':
    # nums = [0, -1, 2, -5 ,9]
    nums = []
    print(Solution().merge_sort(nums))