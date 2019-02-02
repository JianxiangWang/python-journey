# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 347_Top_K_Frequent Elements file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1. Count the frequent.
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        # 2. To list
        counter = counter.items()

        # 3. Build the heap.
        heap = []
        for key, freq in counter:
            if len(heap) < k:
                heapq.heappush(heap, (freq, key))
            else:
                min_freq, _ = heap[0]
                if freq > min_freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq, key))

        # 4. Get the result.
        res = []
        for _ in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        res = res[::-1]
        return res


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
