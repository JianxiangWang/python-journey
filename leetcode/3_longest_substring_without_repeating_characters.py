
"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        O(N^2)
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        n = len(s)
        ans = 1
        for i in range(n):
            for j in range(i + 1, n):
                if len(s[i: j + 1]) == len(set(s[i: j + 1])):
                    ans = max(len(s[i: j + 1]), ans)
        return ans

    def engthOfLongestSubstring_slide_window(self, s):
        """
        O(N)
        """
        ans, window = 0, set()
        i, j = 0, 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in window:
                window.add(s[j])
                ans = max(ans, len(window))
                j += 1
            else:
                window.remove(s[i])
                i += 1
        return ans

    def lengthOfLongestSubstring_slide_window_better(self, s):
        ans, i, char2idx = 0, 0, {}
        for j, char in enumerate(s):
            if s[j] in char2idx and char2idx[char] >= i:
                i = char2idx[char] + 1
            char2idx[s[j]] = j
            ans = max(ans, j - i + 1)
        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring_slide_window_better("abcabcbb"))
