"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Easy
# Most Liked

# Array
# Negate right indexed value

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            right_ind = abs(n) - 1
            nums[right_ind] = -nums[right_ind] if nums[right_ind] > 0 else nums[right_ind]

        res = [i+1 for i, n in enumerate(nums) if n>0]
        return res
