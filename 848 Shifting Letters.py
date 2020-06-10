"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/shifting-letters/
# Medium

# Prefix Sum
# String


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:

        for i in reversed(range(len(shifts)-1)):
            shifts[i] += shifts[i+1]

        t = ord('a')

        return ''.join([chr(((ord(S[i])-t+shift) % 26) + t) for i, shift in enumerate(shifts)])
