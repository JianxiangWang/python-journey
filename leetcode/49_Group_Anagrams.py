# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 49_Group_Anagrams file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

"""


class Solution:

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in group:
                group[k] = []
            group[k].append(s)
        return list(group.values())

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        ans = []
        for s in strs:
            k = "".join(sorted(s))
            if k not in mapping:
                mapping[k] = len(mapping)
                ans.append([s])
            else:
                ans[mapping[k]].append(s)
        return ans


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))