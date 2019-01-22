# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 31_Next_Permutation file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        found_first_descent = False
        n = len(nums)
        j = n - 2
        prev = nums[-1]
        while j >= 0:
            if nums[j] < prev:
                found_first_descent = True
                break
            prev = nums[j]
            j -= 1

        if found_first_descent:
            i = n - 1
            while i > j:
                if nums[i] > nums[j]:
                    break
                i -= 1
            nums[j], nums[i] = nums[i], nums[j]

        j = j + 1
        i = n - 1
        while j < i:
            nums[i], nums[j] = nums[j], nums[i]
            i -= 1
            j += 1


if __name__ == '__main__':
    s = [5, 4, 3, 0]
    Solution().nextPermutation(s)
    print(s)
