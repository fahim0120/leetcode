"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/product-of-array-except-self/
# Medium
# Facebook
# Most Liked
# Top Interviews


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = len(nums)

        result = [0]*L

        mult = 1
        for i, num in enumerate(nums):
            result[i] = mult
            mult *= num

        mult = 1
        for i in reversed(range(L)):
            result[i] *= mult
            mult *= nums[i]

        return result
