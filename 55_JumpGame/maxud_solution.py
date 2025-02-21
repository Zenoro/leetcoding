class Solution:
    def canJump(self, nums: list[int]) -> bool:
        ln = len(nums)
        if ln == 1 or nums[0] >= ln:
            return True
        else:
            res = [0] * ln
            for i in range(ln):
                for j in range(i + 1, i + 1 + min(nums[i], ln - i - 1)):
                    res[j] += 1
        return all(res[1:])

# solution = Solution()

# print(solution.canJump([2,3,1,1,4]))
# print(solution.canJump([3,2,1,0,4]))
# print(solution.canJump([1,0,1,1]))
# print(solution.canJump([2,0,1,1]))
# print(solution.canJump([1,1,0]))
# print(solution.canJump([3,0,8,2,0,0,1]))

