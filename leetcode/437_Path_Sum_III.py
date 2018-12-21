# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 437_Path_Sum_III file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type s: int
        :rtype: int
        """
        if root is None:
            return 0

        def dfs(node, s):
            res = 0
            if node is None:
                return res
            s -= node.val
            if s == 0:
                res += 1
            res += dfs(node.left, s)
            res += dfs(node.right, s)
            return res

        return dfs(root, s) + self.pathSum(root.left, s) + self.pathSum(root.right, s)




