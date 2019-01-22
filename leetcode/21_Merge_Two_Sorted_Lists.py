# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 21_Merge_Two_Sorted_Lists file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionLinkedList:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: List[int]
        :type l2: List[int]
        :rtype: List[int]
        """
        m, n = len(l1), len(l2)
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        while i < m:
            res.append(l1[i])
            i += 1

        while j < n:
            res.append(l2[j])
            j += 1

        return res


if __name__ == '__main__':
    print(Solution().mergeTwoLists([1, 3, 4], [2, 5, 7]))