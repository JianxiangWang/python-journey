# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 111_Minimum_Depth_of_Binary_Tree file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepthDFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def dfs(node, depth, ans):
            if node.right is None and node.left is None:
                ans.append(depth)
                return
            if node.right:
                dfs(node.right, depth + 1, ans)
            if node.left:
                dfs(node.left, depth + 1, ans)

        ans = []
        dfs(root, 1, ans)
        return min(ans)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left != 0 and right != 0:
            return min(left, right) + 1
        else:
            return left + right + 1

"""
 if (root == null){
            return 0;
}

int left = minDepth(root.left);
int right = minDepth(root.right);

if (left !=0 && right != 0){
    return Math.min(left, right) + 1;
}else {
    return left + right + 1;
}
"""
