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

        '''
        Backtracking
        nums = [1, 2, 3], result = [], curr_subset = []
            nums = [2, 3], result = [[]], curr_subset = [1]
                nums = [3], result = [[], [1]], curr_subset = [1, 2]
                    nums = [], result = [[], [1], [1, 2]], curr_subset = [1, 2, 3]
                        result = [[], [1], [1, 2], [1, 2, 3]]
                nums = [], result = [[], [1], [1, 2], [1, 2, 3]], curr_subset = [1, 3]
                    result = [[], [1], [1, 2], [1, 2, 3], [1, 3]]
            nums = [3], result = [[], [1], [1, 2], [1, 2, 3], [1, 3]], curr_subset = [2]
                nums = [], result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2]], curr_subset = [2, 3]
                    result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
            nums = [], result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]], curr_subset = [3]
                result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        '''
        def backtrack(nums, result, curr_subset):
            result.append(curr_subset)
            for i, num in enumerate(nums):
                backtrack(nums[i+1:], result, curr_subset + [num])

        result = []
        backtrack(nums, result, [])
        return result

        '''
        Backtracking, passing the starting index only
        '''
        def backtrack(nums, result, curr_subset, start):
            result.append(curr_subset)

            for i, num in enumerate(nums[start:], start=start):
                backtrack(nums, result, curr_subset + [num], i+1)

        result = []
        backtrack(nums, result, [], 0)
        return result
