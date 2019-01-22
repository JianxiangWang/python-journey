# coding=utf-8
#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The 17_Letter_Combinations_of_a_Phone_Number file.

Authors: Wang Jianxiang (wangjianxiang01@baidu.com)
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        number_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # letters = [number_to_letter[x] for x in digits]

        def dfs(digits, depth, comb, ans):
            if depth == len(digits):
                ans.append("".join(comb))
                return
            for letter in number_to_letter[digits[depth]]:
                dfs(digits, depth+1, comb + [letter], ans)

        ans = []
        dfs(digits, 0, [], ans)
        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))