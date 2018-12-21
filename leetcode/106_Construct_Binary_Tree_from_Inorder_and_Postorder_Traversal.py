# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 106_Construct_Binary_Tree_from_Inorder_and_Postorder_Traversal file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        k = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[k + 1:], postorder[-1 - len(inorder[k + 1:]): -1])
        root.left = self.buildTree(inorder[:k], postorder[: -1 - len(inorder[k + 1:])])
        return root
