"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/xor-queries-of-a-subarray/
# Medium

# Bit Manipulation

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        N = len(arr)
        ps = [0]*(N+1)

        for i in range(1, N+1):
            ps[i] = ps[i-1] ^ arr[i-1]

        return [ps[l]^ps[r+1] for l, r in queries]
