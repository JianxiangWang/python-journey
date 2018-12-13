# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 100_Same_Tree file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True

        if p is None and q is not None:
            return False

        if p is not None and q is None:
            return False

        if q.val == p.val and self.isSameTree(p.right, q.right) and self.isSameTree(q.left, p.left):
            return True
        else:
            return False