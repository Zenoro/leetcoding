# была идея сделать sliding window
# не уверен, что это тут пойдёт

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        l = 0
        r = 0
        n = len(nums)
        subsum = 0
        counter = 0
        # for r in range(n):
        while l <= n and r <= n: 
            subsum += nums[r]
            if subsum == k:
                counter += 1
            
