# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 206_Reverse_Linked_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseList_recurrent(self, head):

        def _helper(prev, curr):
            if curr:
                nxt = curr.next
                curr.next = prev
                return _helper(curr, nxt)
            else:
                return prev
        return _helper(None, head)