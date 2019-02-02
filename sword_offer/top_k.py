# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The top_k file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""
import heapq


class Solution:
    def topK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    _ = heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return [heapq.heappop(heap) for _ in range(len(heap))][::-1]


def top_k_in_sequence(s, k):
    heap = []
    for i, x in enumerate(s):
        if i < k:
            heapq.heappush(heap, x)
        else:
            smallest = heap[0]
            if x > smallest:
                heapq.heapreplace(heap, x)
    return[heapq.heappop(heap) for _ in range(len(heap))][::-1]




if __name__ == '__main__':
    print(top_k_in_sequence(range(1000), 2))
