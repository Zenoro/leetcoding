from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        if res != -1:
            self.cache.move_to_end(key)
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        
# -------------------- TESTS ------------------------------

# inp1 = ["LRUCache","get","put","get","put","put","get","get"]
# inp2 = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]

# inp1 = ["LRUCache","put","put","get","put","get","put","get","get","get"]
# inp2 = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# inp1 = ["LRUCache","put","put","get","put","get","put","get","get","get"]
# inp2 = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

inp1 = ["LRUCache","put","put","put","put","get","get"]
inp2 = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

def run(commands, values):
    name = commands[0]
    exec(f'{name} = LRUCache({values[0][0]})')
    for func, value in zip(inp1[1:], inp2[1:]):
        print(eval(f'{name}.{func}(*{str(value)})'))

run(inp1, inp2)
