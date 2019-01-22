# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 83_Remove_Duplicates_from_Sorted_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(None)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            nxt = curr.next
            if nxt is None or curr.val != nxt.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        return dummy.next