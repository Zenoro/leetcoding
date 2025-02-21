class Solution:
    def canJump(self, nums: List[int]) -> bool:
        expect = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > expect:
                expect = 0
            elif nums[i] == 0 or expect:
                expect += 1
        return not expect
