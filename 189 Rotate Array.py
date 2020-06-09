"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/rotate-array/
# Easy
# Top Interviews

# Array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], s: int, e: int) -> None:
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        N = len(nums)
        k %= N # in case k > N
        reverse(nums, 0, N-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, N-1)
