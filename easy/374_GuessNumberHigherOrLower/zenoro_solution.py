# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

"""     UNCOMMENT FOR TESTING
def guess(x, target=6):
    if x>target:
        return -1
    elif x<target:
        return 1
    else:
        return 0
"""

class Solution(object):
    def guessNumber(self, n):
        fst, lst = 1, n
        while fst != lst:
            idx = (fst+lst)//2
            res = guess(idx)
            if res == 1:
                fst = idx+1
            elif res == -1:
                lst = idx
            else:
                return idx
        return fst


# print(guessNumber(10))
