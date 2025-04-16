# решение в лоб, возможно есть вариант получше
# плюс без тестов, так что правильно под вопросом

class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.len1 = len(v1)
        self.len2 = len(v2)
        self.iter1 = self.len1
        self.iter2 = self.len2
        self.flag = 1

    """
    @return: An integer
    """
    def _next(self):
        if not self.iter1:
            self.flag = 0
        if not self.iter2:
            self.flag = 1
        if self.flag and self.iter1:
            nxt = self.v1[self.len1 - self.iter1]
            self.flag = 0
            self.iter1 -= 1
            return nxt
        if not self.flag and self.iter2:
            nxt = self.v2[self.len2 - self.iter2]
            self.flag = 1
            self.iter2 -= 1
            return nxt
        
    """
    @return: True if has next
    """
    def hasNext(self):
        return self.iter1 > 0 or self.iter2 > 0

v1 = [3, 4, 5, 6]
v2 = [1, 2]

solution, result = ZigzagIterator(v1, v2), []
while solution.hasNext(): result.append(solution._next())
print(result)