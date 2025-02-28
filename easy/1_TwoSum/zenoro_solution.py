class Solution(object):
    def twoSum(self, nums, target):
        numset = {}
        for idx, num in enumerate(nums):
            if target - num in numset:
                return [numset[target - num], idx]
            numset[num] = idx


# nums = [2,7,11,15]; target = 9
# print(Solution().twoSum(nums, target))

# nums = [3,3]; target = 6
# print(Solution().twoSum(nums, target))

# nums = [3,2,4]; target = 6
# print(Solution().twoSum(nums, target))
