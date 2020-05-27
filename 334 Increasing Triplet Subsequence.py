"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/increasing-triplet-subsequence/
# Medium
# Top Interviews


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1 = num2 = float('inf')

        for n in nums:
            if n <= num1:
                num1 = n
            elif n <= num2:
                num2 = n
            else:
                return True

        return False
