class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        res = 1
        for elem in nums:
            summ += elem
            if summ < 0:
                summ = 0
            res = max(res, summ)
        return res
