"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/
# Medium
# LinkedIn
# Most Liked
# Top Interviews


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        s = e = -1
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            M = nums[m]

            if target == M:
                s = m
                r = m - 1
            elif target < M:
                r = m - 1
            else:
                l = m + 1

        if s == -1:
            return [-1, -1]

        l, r = s, len(nums)-1
        while l <= r:
            m = (l+r)//2
            M = nums[m]

            if target == M:
                e = m
                l = m + 1
            elif target < M:
                r = m - 1
            else:
                l = m + 1

        return [s, e]

