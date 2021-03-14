"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/game-of-life/
# Medium
# Top Interviews


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        H, W = len(board), len(board[0])

        def get_alive_neighbors(r: int, c: int) -> int:
            neighbors = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

            live_neighbors = 0

            for dr, dc in neighbors:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < H and 0 <= nc < W and abs(board[nr][nc]) == 1:
                    live_neighbors += 1

            return live_neighbors


        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                live_neighbors = get_alive_neighbors(r, c)

                if cell == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2


        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == -1:
                    board[r][c] = 0
                elif cell == 2:
                    board[r][c] = 1
