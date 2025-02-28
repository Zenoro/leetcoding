class Solution(object):
    def twoSum(self, nums:list, target):
        for idx in range(len(nums)-1):
            elem = nums[idx]
            s = set(nums[idx+1:])
            if target - elem in s:
                for idx2, elem2 in enumerate(nums[idx+1:]):
                    if elem2 == target - elem:
                        return [idx, idx2+idx+1]


# nums = [2,7,11,15]; target = 9
# print(Solution().twoSum(nums, target))

# nums = [3,3]; target = 6
# print(Solution().twoSum(nums, target))

# nums = [3,2,4]; target = 6
# print(Solution().twoSum(nums, target))
