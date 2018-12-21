# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 113_Path_Sum_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
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
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        def dfs(node, path_nodes, ans):
            path_nodes = path_nodes + [node.val]
            if node.left is None and node.right is None:
                if sum(path_nodes) == s:
                    ans.append(path_nodes)
                return
            if node.left:
                dfs(node.left, path_nodes, ans)
            if node.right:
                dfs(node.right, path_nodes, ans)

        ans = []
        dfs(root, [], ans)
        return ans