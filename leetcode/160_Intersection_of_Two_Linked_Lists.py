# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 160_Intersection_of_Two_Linked_Lists file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

"""
import utils

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        lengthA = self._get_length(headA)
        lengthB = self._get_length(headB)
        if lengthA < lengthB:
            lengthA, lengthB = lengthB, lengthA
            headA, headB = headB, headA

        for _ in range(lengthA - lengthB):
            headA = headA.next

        pointerA, pointerB = headA, headB
        while pointerA and pointerB:
            if pointerA is pointerB:
                return pointerA
            pointerA = pointerA.next
            pointerB = pointerB.next

        return None

    def _get_length(self, head):
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return n

    def getIntersectionNode2(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        new_headA = self._reverse(headA)
        new_headB = self._reverse(headB)
        a_pointer, b_pointer = new_headA, new_headB
        prev = None
        while a_pointer and b_pointer:
            if a_pointer.val != b_pointer.val:
                return prev
            else:
                prev = a_pointer
            a_pointer = a_pointer.next
            b_pointer = b_pointer.next

        return prev

    def _reverse(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


if __name__ == '__main__':
    headA = utils.build_linked_list_from_list([1, 2, 3, 4, 5])
    headB = utils.build_linked_list_from_list([1, 2, 3, 4, 5])
    x = Solution().getIntersectionNode(headA, headB)
    print(x.val)

