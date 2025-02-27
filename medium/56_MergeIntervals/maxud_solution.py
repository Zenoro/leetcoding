class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            b1, e1 = res.pop()
            b2, e2 = interval
            if b2 >= b1 and b2 <= e1:
                res.append([b1, max(e1, e2)])
            else:
                res.extend([[b1, e1], interval])
        return res