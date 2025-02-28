class Solution(object):
    def searchMatrix(self, matrix, target):
        return any([target in strok for strok in matrix])

