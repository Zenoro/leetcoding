class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_to = 0
        zeros = 0
        for num in nums:
            if num:
                nums[insert_to] = num
                insert_to += 1
            else:
                zeros += 1
        for i in range(insert_to, insert_to + zeros):
            nums[i] = 0
