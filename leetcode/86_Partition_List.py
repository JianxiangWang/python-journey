# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 86_Partition_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

"""
import utils


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        less_dummy_head, greater_dummy_head = ListNode(None), ListNode(None)

        less_pointer, greater_pointer = less_dummy_head, greater_dummy_head
        curr = head
        while curr:
            if curr.val < x:
                less_pointer.next = curr
                less_pointer = curr
            else:
                greater_pointer.next = curr
                greater_pointer = curr
            curr = curr.next
            less_pointer.next = None
            greater_pointer.next = None

        less_pointer.next = greater_dummy_head.next
        return less_dummy_head.next


if __name__ == '__main__':
    head = utils.build_linked_list_from_list([1,4,3,2,5,2])
    new_head = Solution().partition(head, 3)
    utils.print_linked_list(new_head)


