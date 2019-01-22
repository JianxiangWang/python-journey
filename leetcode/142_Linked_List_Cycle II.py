# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 142_Linked_List_Cycle II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        slow, fast = head, head
        meet = False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                meet = True
                break
        if not meet:
            return None
        else:
            curr = head
            while curr != slow:
                curr = curr.next
                slow = slow.next
            return curr


    def detectCycle_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            else:
                visited.add(curr)
            curr = curr.next

        return None

