# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 345_Reverse_Vowels_of_a_String file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""

"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "e", "i", "o", "u"}

        s_lst = list(s)
        i, j = 0, len(s) - 1
        while i <= j:
            if s_lst[i].lower() not in vowels:
                i += 1
            elif s_lst[j].lower() not in vowels:
                j -= 1
            else:
                s_lst[i], s_lst[j] = s_lst[j], s_lst[i]
                i += 1
                j -= 1

        return "".join(s_lst)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))