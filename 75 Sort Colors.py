"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/sort-colors/
# Medium
# Most Liked
# Top Interviews

# Array
# Two Pointers
# Sort
# Dutch Flag Partitioning Problem

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # constants
        RED, WHITE, BLUE = 0, 1, 2

        # pointers
        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] == RED:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == WHITE:
                w += 1
            elif nums[w] == BLUE:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
