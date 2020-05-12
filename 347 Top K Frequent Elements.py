"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/top-k-frequent-elements/
# Medium
# Amazon
# Most Liked
# Top Interviews

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d = Counter(nums)
        return heapq.nlargest(k, d.keys(), key=d.get)


'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        d = Counter(nums)
        return [item[0] for i, item in enumerate(d.most_common()) if i < k]
'''
