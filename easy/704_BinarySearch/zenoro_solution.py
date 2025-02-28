class Solution(object):
    def search(self, nums, target):
        fst, lst = 0, len(nums)
        while fst != lst:
            if len(nums[fst:lst])==1:
                return 0 if target in nums else -1
            idx = (fst+lst)//2
            if nums[idx] < target:
                fst = idx
            elif nums[idx] > target:
                lst = idx
            else:
                return idx
        return -1


# nums = [-1,0,3,5,9,12]
# target = 9
# print(Solution().search(nums, target))

# nums = [-1,0,3,5,9,12]
# target = 2
# print(Solution().search(nums, target))

# nums = [2]
# target = 2
# print(Solution().search(nums, target))

# nums = [2]
# target = 5
# print(Solution().search(nums, target))
