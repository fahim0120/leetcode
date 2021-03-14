"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/palindrome-partitioning/
# Medium
# Top Interviews


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(s: str, path: List[str], result: List[List[str]]):
            if not s:
                result.append(path)

            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    backtrack(s[i:], path + [s[:i]], result)

        result = []
        backtrack(s, [], result)
        return result
