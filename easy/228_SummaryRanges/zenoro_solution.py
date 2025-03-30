from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [str(*nums)]
        else:
            nums.append(-10000)
            res = []
            prev = 0
            is_range = False
            for idx, elem in enumerate(nums[1:]):
                if elem - nums[idx] == 1:
                    is_range = True
                else:
                    if is_range:
                        res.append("->".join(map(str, [nums[prev], nums[idx]])))
                    else:
                        res.append(str(nums[idx]))
                    is_range = False
                    prev = idx + 1
            return res


S = Solution()

# nums = [0,1,2,4,5,7]
# print(S.summaryRanges(nums))

# nums = [0,2,3,4,6,8,9]
# print(S.summaryRanges(nums))


# nums = [-1]
# print(S.summaryRanges(nums))
