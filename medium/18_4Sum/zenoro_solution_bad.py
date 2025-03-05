from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        dd = {}
        res = set()
        for i in range(len(nums)):
            dd[nums[i]] = i

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    buf = target - nums[i] - nums[j] - nums[k]
                    if buf in dd and (dd[buf] != i and dd[buf] != k and dd[buf] != j):
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], buf])))
        return [list(elem) for elem in list(res)]


# nums = [1, 0, -1, 0, -2, 2]; target = 0
# print(Solution().fourSum(nums, target))

# nums = [2,2,2,2,2]; target = 8
# print(Solution().fourSum(nums, target))
