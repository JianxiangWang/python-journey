# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The util file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __cmp__(self, other):
        return self.val < other.val


def build_linked_list_from_list(lst):
    dummy = ListNode(None)
    curr = dummy
    for x in lst:
        node = ListNode(x)
        curr.next = node
        curr = node
    return dummy.next


def print_linked_list(head):
    res = []
    p = head
    while p:
        res.append(p.val)
        p = p.next
    print("-->".join(map(str, res)))
