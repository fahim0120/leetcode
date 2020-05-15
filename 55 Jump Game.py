"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/jump-game/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cur = len(nums) - 1
        i = cur - 1

        while i >= 0:
            if cur - i <= nums[i]:
                cur = i

            i -= 1

        if cur == 0:
            return True

        return False
