# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 19_Remove_Nth_Node_From_End_of_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""
import utils


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


if __name__ == '__main__':
    head = utils.build_linked_list_from_list([1, 2])
    utils.print_linked_list(head)
    new_head = Solution().removeNthFromEnd(head, 1)
    utils.print_linked_list(new_head)


