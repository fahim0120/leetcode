"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Medium

# Array
# Negate right indexed value

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            right_ind = abs(n) - 1
            if nums[right_ind] < 0:
                res.append(abs(n))
            else:
                nums[right_ind] *= -1

        return res
