"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/combination-sum-ii/
# Medium


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(sm: int, start_at: int, path: List[int], result: List[int]) -> None:

            for i, num in enumerate(candidates[start_at:], start=start_at):
                #print(start_at, path, num)
                if i == start_at or num != candidates[i-1]:
                    if sm+num == target:
                        result.append(path+[num])

                    if sm+num < target:
                        helper(sm+num, i+1, path+[num], result)


        candidates.sort()
        result = []
        helper(0, 0, [], result)
        return result
