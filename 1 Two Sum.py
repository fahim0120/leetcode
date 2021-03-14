"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/two-sum/
# Easy
# Amazon
# Google
# Most Liked
# Top Interviews

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()

        for i, num in enumerate(nums):
            if num in my_dict:
                return [my_dict[num], i]
            else:
                my_dict[target-num] = i
