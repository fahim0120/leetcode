"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/word-search/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(word: str, r: int, c: int):
            if not word:
                return True

            if board[r][c] == word[0]:
                board[r][c] = '#'

                # no more letter
                if not word[1:]:
                    return True

                # up
                if r > 0 and board[r-1][c] == word[1]:
                    if dfs(word[1:], r-1, c):
                        return True

                # down
                if r < R-1 and board[r+1][c] == word[1]:
                    if dfs(word[1:], r+1, c):
                        return True

                #left
                if c > 0 and board[r][c-1] == word[1]:
                    if dfs(word[1:], r, c-1):
                        return True

                #right
                if c < C-1 and board[r][c+1] == word[1]:
                    if dfs(word[1:], r, c+1):
                        return True

                board[r][c] = word[0]

        for r in range(0, R):
            for c in range(0, C):
                if dfs(word, r, c):
                    return True
        return False
