"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/rotate-image/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''
        vertical flip
            A.B  -> D.C
            . .     . .
            D.C     A.B
        '''
        matrix.reverse()

        '''x
        diagonal flip
            D.C -> D.A
            . .    . .
            A.B    C.B
        '''
        n = len(matrix) - 1
        for i in range(n+1):
            for j in range(i+1, n+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

