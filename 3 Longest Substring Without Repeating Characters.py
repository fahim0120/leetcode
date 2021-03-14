"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        indices = {}

        max_len = 0
        start = 0

        for i, c in enumerate(s):
            if c in indices:
                last = indices[c]

                if last >= start:
                    max_len = max(max_len, i-start)

                    start = last + 1

            indices[c] = i

        max_len = max(max_len, len(s)-start)

        return max_len
