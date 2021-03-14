"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/container-with-most-water/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0

        while i < j:
            w = j - i
            h = min(height[i], height[j])

            max_area = max(max_area, w*h)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
