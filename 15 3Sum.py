"""
 fahim0120@gmail.com
"""
# https://leetcode.com/problems/3sum/
# Medium
# Most Liked
# Top Interviews


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            j = i+1
            k = len(nums)-1

            if i > 0 and nums[i-1] == a:
                continue

            while j < k:
                if j == i+1 or nums[j] != nums[j-1]:
                    b, c = nums[j], nums[k]
                    s = a + b + c
                    if s == 0:
                        ans.append([a, b, c])
                        j += 1
                    elif s > 0:
                        k -= 1
                    else:
                        j += 1
                else:
                    j += 1
        return ans

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # print(nums)
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                b, c = nums[j], nums[k]
                s = a + b + c

                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                elif s == 0:
                    ans.append([a, b, c])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1

                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1

        return ans
"""
