"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/generate-parentheses/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(s, e, path, result):
            if s == e == n:
                result.append(path)
                return

            if s < n:
                backtrack(s+1, e, path+'(', result)

            if e < s:
                backtrack(s, e+1, path+')', result)


        result = []
        backtrack(0, 0, '', result)
        return result
