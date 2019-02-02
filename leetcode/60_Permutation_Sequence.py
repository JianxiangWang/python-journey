# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 60_Permutation_Sequence file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = list(range(1, n+1))
        comb = []
        k = k - 1
        while len(comb) < n:
            step = self.factorial(len(nums) - 1)
            i = k // step
            k = k % step
            comb.append(nums[i])
            nums = nums[:i] + nums[i+1:]
        return "".join(map(str, comb))

    def factorial(self, n):
        res = 1
        while n > 1:
            res *= n
            n -= 1
        return res


if __name__ == '__main__':
    print(Solution().getPermutation(4, 9))
