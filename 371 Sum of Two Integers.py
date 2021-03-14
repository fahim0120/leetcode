"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/sum-of-two-integers/
# Easy
# Top Interviews

# Bit Manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF # 32 1s

        while b & MASK != 0:
            a, b = a^b, (a&b) << 1 # a <- sum; b <- carry

        return a & MASK if b else a
