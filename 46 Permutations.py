"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/permutations/
# Medium
# LinkedIn
# Most Liked
# Top Interviews


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]

        result = []
        for i, num in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i+1:]):
                result.append([num] + p)

        return result
