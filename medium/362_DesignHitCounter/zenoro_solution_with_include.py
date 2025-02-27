from collections import defaultdict

class HitCounter:

    def __init__(self):
        self.hits = defaultdict(int)

    def hit(self, timestamp: int):
        self.hits[timestamp] += 1

    def get_hits(self, timestamp: int) -> int:
        return sum([self.hits[elem] for elem in self.hits if elem in range(timestamp-299, timestamp+1)])

