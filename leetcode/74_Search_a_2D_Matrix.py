# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 74_Search_a_2D_Matrix file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        first_column = [row[0] for row in matrix]
        lo, hi = 0, len(first_column) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if first_column[mid] == target:
                return True
            elif first_column[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        if hi < 0:
            return False

        selected_row = matrix[hi]
        lo, hi = 0, len(selected_row) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if selected_row[mid] == target:
                return True
            elif selected_row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        r, c = len(matrix), len(matrix[0])
        n = r * c

        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            r_idx, c_idx = mid // c, mid % c
            if target == matrix[r_idx][c_idx]:
                return True
            elif target < matrix[r_idx][c_idx]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(Solution().searchMatrix(matrix, 50))
