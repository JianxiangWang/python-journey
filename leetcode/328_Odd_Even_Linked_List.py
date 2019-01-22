# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 328_Odd_Even_Linked_List file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

"""
import utils

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd_dummy, even_dummy = ListNode(None), ListNode(None)
        odd_pointer, even_pointer = odd_dummy, even_dummy
        curr, i = head, 0
        while curr:
            if i % 2 == 0:
                odd_pointer.next = curr
                odd_pointer = curr
                curr = curr.next
                odd_pointer.next = None
            else:
                even_pointer.next = curr
                even_pointer = curr
                curr = curr.next
                even_pointer.next = None
            i += 1

        odd_pointer.next = even_dummy.next
        return odd_dummy.next


if __name__ == '__main__':
    head = utils.build_linked_list_from_list([1, 2, 3, 4, 5])
    utils.print_linked_list(head)
    new_head = Solution().oddEvenList(head)
    utils.print_linked_list(new_head)




