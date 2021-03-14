"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/compare-version-numbers/
# Medium


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))

        for x, y in itertools.zip_longest(v1, v2, fillvalue=0):
            if x < y:
                return -1
            elif x > y:
                return 1

        return 0
