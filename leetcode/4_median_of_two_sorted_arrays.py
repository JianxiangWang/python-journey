# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 4_median_of_two_sorted_arrays file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        ans = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                ans.append(nums1[i])
                if (m + n) % 2 == 1 and len(ans) == int((m + n) / 2) + 1:
                    return ans[-1]
                if (m + n) % 2 == 0 and len(ans) == int((m + n) / 2) + 1:
                    return (ans[-1] + ans[-2]) / 2.0
                i += 1
            else:
                ans.append(nums2[j])
                if (m + n) % 2 == 1 and len(ans) == int((m + n) / 2) + 1:
                    return ans[-1]
                if (m + n) % 2 == 0 and len(ans) == int((m + n) / 2) + 1:
                    return (ans[-1] + ans[-2]) / 2.0
                j += 1

        for k in range(i, m):
            ans.append(nums1[k])
            if (m + n) % 2 == 1 and len(ans) == int((m + n) / 2) + 1:
                return ans[-1]
            if (m + n) % 2 == 0 and len(ans) == int((m + n) / 2) + 1:
                return (ans[-1] + ans[-2]) / 2.0

        for k in range(j, n):
            ans.append(nums2[k])
            if (m + n) % 2 == 1 and len(ans) == int((m + n) / 2) + 1:
                return ans[-1]
            if (m + n) % 2 == 0 and len(ans) == int((m + n) / 2) + 1:
                return (ans[-1] + ans[-2]) / 2.0

    def findMedianSortedArrays_binary_search(self, nums1, nums2):
        """
        O(log(min(m, n)))
        :param nums1:
        :param nums2:
        :return:
        """
        A, B = nums1, nums2
        m, n = len(nums1), len(nums2)
        if m > n:
            A, B = B, A
            m, n = n, m

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            if i < m and A[i] < B[j - 1]:
                low = i + 1
            elif i > 0 and B[j] < A[i - 1]:
                high = i - 1
            else:
                if i == 0:
                    left_max = B[j - 1]
                elif j == 0:
                    left_max = A[i - 1]
                else:
                    left_max = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return left_max

                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])

                return (left_max + right_min) / 2.


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays_binary_search([3], [1, 2, 4]))
