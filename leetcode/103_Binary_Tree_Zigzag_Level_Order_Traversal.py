# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 103_Binary_Tree_Zigzag_Level_Order_Traversal file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        idx = 0
        res = []
        nodes = [root]
        while nodes:
            if idx % 2 == 0:
                res.append([x.val for x in nodes])
            else:
                res.append([x.val for x in nodes][::-1])

            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes

            idx += 1

        return res