# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 143_Reorder——List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""
import utils


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        new_head = slow.next
        slow.next = None

        # 2. Reverse.
        prev, curr = None, new_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        new_head = prev

        # 3. Merge.
        p, q = head, new_head
        while q:
            p_next, q_next = p.next, q.next
            p.next = q
            q.next = p_next
            p = p_next
            q = q_next








    def reorderList_recur(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        dummy = ListNode(None)
        dummy.next = head

        prev, curr = dummy, head
        while curr.next:
            curr = curr.next
            prev = prev.next

        if curr == head:
            return

        if prev == head:
            return

        next_head = head.next
        head.next = curr
        curr.next = next_head
        prev.next = None
        self.reorderList(next_head)


if __name__ == '__main__':
    head = utils.build_linked_list_from_list([1,2,3,4,5])
    utils.print_linked_list(head)
    Solution().reorderList(head)
    utils.print_linked_list(head)



