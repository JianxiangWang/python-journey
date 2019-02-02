# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 448_Find_All_Numbers_Disappeared_in_an_Array file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

"""


class Solution:

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ 正负号标记法 """

        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
               ans.append(i + 1)
        return ans


    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        参考41题
        """

        if not nums:
            return []
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        print(nums)
        res = []
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers2([4,3,2,7,8,2,3,1]))
