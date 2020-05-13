"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Medium
# Facebook
# LinkedIn
# Most Liked
# Top Interviews


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            M = (L + R)//2
            l, m, r = nums[L], nums[M], nums[R]

            if target == m:
                    return M

            if l <= m:
                if l <= target < m:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if m < target <= r:
                    L = M + 1
                else:
                    R = M - 1

        return -1
