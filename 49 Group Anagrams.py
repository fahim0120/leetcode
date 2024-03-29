"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/group-anagrams/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = collections.defaultdict(list)

        for s in strs:
            groups[str(sorted(s))].append(s)

        return groups.values()
