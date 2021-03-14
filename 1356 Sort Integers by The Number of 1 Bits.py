"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Easy

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_set_bits(n):
            count = 0
            while n:
                n = n & (n-1)
                count += 1

            return count

        arr.sort(key = lambda x: (count_set_bits(x), x))
        return arr
