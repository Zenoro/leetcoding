class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        res = []
        first = nums[0]
        last = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                last = nums[i + 1]
            elif first != last:
                res.append(str(first) + '->' + str(last))
                first = nums[i + 1]
                last = nums[i + 1]
            else:
                res.append(str(first))
                first = nums[i + 1]
                last = nums[i + 1]
        if first != last:
            res.append(str(first) + '->' + str(last))
        else:
            res.append(str(first))
        return res