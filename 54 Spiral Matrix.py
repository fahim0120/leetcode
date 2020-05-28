"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/spiral-matrix/
# Medium
# Top Interviews


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        spiral = []

        tb = lb = 0 # top boundary and left boundary
        bb = len(matrix) - 1 # bottom boundary
        rb = len(matrix[0]) - 1 # right boundary

        direction = 0

        while lb <= rb and tb <= bb:

            if direction == 0: # 'right'
                spiral += matrix[tb][lb:rb+1]
                tb += 1
            elif direction == 1: # 'down'
                spiral += [matrix[i][rb] for i in range(tb, bb+1)]
                rb -= 1
            elif direction == 2: # 'left'
                spiral += matrix[bb][lb:rb+1][::-1]
                bb -= 1
            elif direction == 3: # 'up'
                spiral += [matrix[i][lb] for i in range(bb, tb-1, -1)]
                lb += 1

            direction += 1
            direction %= 4

        return spiral
