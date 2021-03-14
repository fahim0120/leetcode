"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/flood-fill/
# Easy
# Amazon


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        l, r = 0, len(image[0])
        u, d = 0, len(image)
        old = image[sr][sc]
        if old == newColor:
            return image

        def dfs(sr, sc):
            image[sr][sc] = newColor

            if sr+1 < d and image[sr+1][sc] == old:
                dfs(sr+1, sc)
            if sr-1 >= 0 and image[sr-1][sc] == old:
                dfs(sr-1, sc)

            if sc+1 < r and image[sr][sc+1] == old:
                dfs(sr, sc+1)

            if sc-1 >= 0 and image[sr][sc-1] == old:
                dfs(sr, sc-1)

        dfs(sr, sc)
        return image
