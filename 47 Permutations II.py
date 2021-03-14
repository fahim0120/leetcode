"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/permutations-ii/
# Medium


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        seen = set()
        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                for p in self.permuteUnique(nums[:i] + nums[i+1:]):
                    result.append([num] + p)

        return result
