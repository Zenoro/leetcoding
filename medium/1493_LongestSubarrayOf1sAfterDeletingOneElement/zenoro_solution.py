from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lst_idx, zero, res = 0, 0, 0

        for idx in range(len(nums)):
            if nums[idx] == 0:
                zero += 1
                if zero > 1:
                    lst_idx = buf_idx + 1
                    zero -= 1
                buf_idx = idx
            window = idx - lst_idx
            res = max(res, window)
        return res
    
# nums = [0,1,1,1,0,1,1,0,1]
# print(Solution().longestSubarray(nums))

# nums = [1,1,0,1]
# print(Solution().longestSubarray(nums))

# nums = [1,1,1]
# print(Solution().longestSubarray(nums))
