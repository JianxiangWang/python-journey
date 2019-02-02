# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 23_Merge_k_Sorted_Lists file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import utils
import heapq
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        """
        Should run in python2 !
        """

        dummy = ListNode(None)
        curr = dummy

        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))

        while not q.empty():
            _, node = q.get()
            if node.next:
                q.put((node.next.val, node.next))
            curr.next = node
            node = node.next
            curr = curr.next
            curr.next = None

        return dummy.next

    def mergeKLists_2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        O(KN).
        """
        dummy = ListNode(None)
        curr = dummy
        while True:
            min_i = -1
            for i, head in enumerate(lists):
                if not head:
                    continue
                if min_i == -1 or head.val < lists[min_i].val:
                    min_i = i
            if min_i == -1:
                break
            curr.next = lists[min_i]
            lists[min_i] = lists[min_i].next
            curr = curr.next
            curr.next = None

        return dummy.next




if __name__ == '__main__':
    # h1 = utils.build_linked_list_from_list([1, 2, 3, 4])
    # h2 = utils.build_linked_list_from_list([2, 4, 7])
    # ans = Solution().mergeKLists([h1, h2])
    # utils.print_linked_list(ans)
    print(ListNode(1) > ListNode(10))
