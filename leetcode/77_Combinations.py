# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 77_Combinations file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(nodes, depth, comb, res):
            if depth > k:
                return

            if depth == k:
                res.append(comb)

            for i, node in enumerate(nodes):

                # Return if max depth can not reach k. Good !
                max_depth = depth + len(nodes) - i
                if max_depth < k:
                    return

                dfs(nodes[i+1:], depth+1, comb+[node], res)

        res = []
        dfs(range(1, n+1), 0, [], res)
        return res


if __name__ == '__main__':
    print(Solution().combine(4, 2))