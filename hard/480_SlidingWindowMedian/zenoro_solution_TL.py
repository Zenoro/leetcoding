class Solution:
    def medianSlidingWindow(self, nums, k):
        res = []
        for i in range(len(nums)-k+1):
            wnd = sorted(nums[i:i+k])
            if k%2==0:
                res.append((wnd[k//2] + wnd[k//2-1]) / 2)
            else:
                res.append(wnd[k//2])
        return res


nums = [1,3,-1,-3,5,3,6,7]; k = 3
print(Solution().medianSlidingWindow(nums, k))
