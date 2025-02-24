
def findClosestNumber(nums) -> int:
    prev = nums[-1]
    for elem in nums[len(nums)-2::-1]:
        if abs(elem) < abs(prev):
            prev = elem
        else:
            return prev
    return prev
