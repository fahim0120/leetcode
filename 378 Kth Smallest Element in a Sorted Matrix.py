"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Medium
# Top Interviews


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for row in matrix:
            lst.extend(row)

        return nsmallest(k, lst)[-1]


'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            for n in row:
                if len(heap) < k:
                    heapq.heappush(heap, -n)
                elif heap[0] < -n:
                    heapq.heappushpop(heap, -n)

        return -heap[0]
'''
