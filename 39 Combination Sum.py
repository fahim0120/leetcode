"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/combination-sum/
# Medium
# Most Liked


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(sm, start_at, path, result):
            for i, num in enumerate(candidates[start_at:], start=start_at):
                if sm + num == target:
                    result.append(path + [num])

                if sm + num < target:
                    helper(sm+num, i, path + [num], result)


        result = []
        helper(0, 0, [], result)
        return result
