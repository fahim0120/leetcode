"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/24-game/
# Hard
# Google

# Depth-first Search
# Backtracking

"""
4 numbers and 4 operators (parenthesis for picking a ordered pair of numbers)
-> constant number of operations
-> try backtracking
"""

class Solution:
    from operator import truediv, mul, add, sub

    def judgePoint24(self, nums: List[int]) -> bool:

        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6

        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j:
                    rest = [c for k, c in enumerate(nums) if i != k != j]

                    for op in (truediv, mul, add, sub):

                        # to avoid commutative repeatation
                        if op in (mul, add) and i < j:
                            continue

                        # to avoid ZeroDivision
                        try:
                            rest.append(op(a, b))

                            if self.judgePoint24(rest):
                                return True

                            rest.pop()
                        except:
                            pass
        return False
