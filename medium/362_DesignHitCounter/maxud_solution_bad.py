class HitCounter:

    def __init__(self):
        self.hits = []
    
    """
    @param timestamp: the timestamp
    @return: nothing
    """
    def hit(self, timestamp: int):
        # не очень хорошее решение
        try:
            last_ts, amount = self.hits.pop()
        except IndexError:
            self.hits.append((timestamp, 1))
            return

        if last_ts == timestamp:
            self.hits.append((timestamp, amount + 1))
        else:
            self.hits.extend([(last_ts, amount), (timestamp, 1)])
        

    """
    @param timestamp: the timestamp
    @return: the count of hits in recent 300 seconds
    """
    def get_hits(self, timestamp: int) -> int:
        # print(self.hits)
        res = 0
        for ts, amount in self.hits:
            if ts > timestamp - 300:
                res += amount
        return res
