"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/
# Medium
# Most Liked
# Top Interviews

# Array
# Backtracking
# Bit Manipulation


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Bit Manipulation
        Example input : [1, 2, 3]

        3 numbers.
        2 ** 3       = 8  = 0b1000
        (2 ** 4) - 1 = 15 = 0b1111
        bins(bits)[3:] -> 000, 001, ..., 111
        '''
        def helper(nums: List[int], n: int) -> List[int]:
            bits = bin(n)[3:]
            return [nums[i] for i, c in enumerate(bits) if c == '1']

        N = len(nums)
        return [helper(nums, i) for i in range(2**N, 2**(N+1))]
