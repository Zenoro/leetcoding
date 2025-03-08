from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fst, lst = 0, len(numbers)-1
        while fst < lst:
            if numbers[fst] + numbers[lst] == target:
                return [fst+1, lst+1]
            elif numbers[fst] + numbers[lst] < target:
                fst += 1
            else:
                lst -= 1
            

# numbers = [2,7,11,15]; target = 9
# print(Solution().twoSum(numbers, target))

# numbers = [2,3,4]; target = 6
# print(Solution().twoSum(numbers, target))

# numbers = [-1,0]; target = -1
# print(Solution().twoSum(numbers, target))

# numbers = [5,25,75]; target = 100
# print(Solution().twoSum(numbers, target))
