# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 82_Remove_Duplicates_from_Sorted_List_II file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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

        dummy = ListNode(None)
        dummy.next = head

        prev, curr = dummy, head
        should_skip = False
        while curr:
            nxt = curr.next
            if nxt is None or nxt.val != curr.val:
                if not should_skip:
                    prev.next = curr
                    prev = curr
                else:
                    prev.next = None
                should_skip = False
            else:
                should_skip = True
            curr = curr.next

        return dummy.next


def _build_linked_list_from_list(lst):
    dummy = ListNode(None)
    curr = dummy
    for x in lst:
        node = ListNode(x)
        curr.next = node
        curr = node
    return dummy.next


def _print_linked_list(head):
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    print("-->".join(map(str, res)))


if __name__ == '__main__':
    head = _build_linked_list_from_list([1, 2, 3, 3, 4, 4, 5])
    _print_linked_list(head)
    new_head = Solution().deleteDuplicates(head)
    _print_linked_list(new_head)