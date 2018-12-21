# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 114_Flatten_Binary_Tree_to_Linked_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        def dfs(node, visited):
            if node is None:
                return
            visited.append(node)
            if node.left:
                dfs(node.left, visited)
            if node.right:
                dfs(node.right, visited)

        visited = []
        dfs(root, visited)
        for i in range(len(visited) - 1):
            visited[i].left = None
            visited[i].right = visited[i + 1]
