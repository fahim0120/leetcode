"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Medium


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # O(log n) solution

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l)//2

            if l == r:
                return nums[l]

            if m%2 == 1:
                m -= 1

            if nums[m] != nums[m+1]:
                r = m
            else:
                l = m + 2


        return nums[l]

        '''
        O(n) solution
        sm = 0
        for num in nums:
            sm ^= num

        return sm
        '''
