# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 24_Swap_Nodes_in_Pairs file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        nxt = head.next
        head.next = self.swapPairs(head.next.next)
        nxt.next = head

        return nxt

    def swapPairs_dummy(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy
        while curr.next and curr.next.next:
            next_one, next_two, next_three = curr.next, curr.next.next, curr.next.next
            curr.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            curr = next_one

        return dummy.next
