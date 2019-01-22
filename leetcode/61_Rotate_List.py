# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 61_Rotate_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        c = n - k % n
        dummy = ListNode(None)
        dummy.next = head

        curr, i = dummy, 0
        p, q, v = None, None, None
        while curr:
            if i == c:
                p = curr
            if i == c + 1:
                q = curr
            if i == n:
                v = curr
            i += 1
            curr = curr.next

        if q is None:
            return dummy.next
        else:
            p.next = None
            v.next = dummy.next
            return q



