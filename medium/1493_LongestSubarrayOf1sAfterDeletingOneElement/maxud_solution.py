class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        longest = 0
        l = 0
        n = len(nums)
        zeros = 0
        last_one = 0
        for r in range(n):
            if nums[r] == 0:
                zeros += 1
                while zeros > 1:
                    l = last_one
                    zeros -= 1
                last_one = r + 1
            w = r - l
            longest = max(longest, w)
        return longest
