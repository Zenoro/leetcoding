class HitCounter:

    def __init__(self):
        self.hits = dict()

    def hit(self, timestamp: int):
        if self.hits.get(timestamp, 0):
            self.hits[timestamp] += 1
        else:
            self.hits[timestamp] = 1

    def get_hits(self, timestamp: int) -> int:
        return sum([self.hits[elem] for elem in self.hits if elem > timestamp - 300])
