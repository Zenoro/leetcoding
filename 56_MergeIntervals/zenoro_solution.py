class Solution:
    def merge(self, interval: List[List[int]]) -> List[List[int]]:
        interval.sort(key=lambda x: x[0])
        lst_interval = interval[0]
        res = []
        for next_idx in range(1, len(interval)):
            if interval[next_idx][0] <= lst_interval[1]:
                lst_interval = [min(lst_interval[0], interval[next_idx][0]), max(lst_interval[1], interval[next_idx][1])]
            else:
                res.append(lst_interval)
                lst_interval = interval[next_idx]
        res.append(lst_interval)
        return res
