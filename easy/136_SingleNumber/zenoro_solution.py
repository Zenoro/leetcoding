class Solution(object):
    def singleNumber(self, nums):
        met = set(nums)

        dd = dict()
        for elem in nums:
            if dd.get(elem, '##') == '##':
                dd[elem] = 0
            else:
                met.remove(elem)
        return list(met)[0]


# rr=[2,2,1]
# print(Solution().singleNumber(rr))

# rr=[4,1,2,1,2]
# print(Solution().singleNumber(rr))
