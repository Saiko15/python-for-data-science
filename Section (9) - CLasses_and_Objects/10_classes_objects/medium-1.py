from tracemalloc import start


class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def has_next(self):
        return self.start < self.end

    def get_next(self):
        ret = self.start
        self.start += self.step
        return ret

rng = MyRange(5,10,1)

while rng.has_next():
    print(rng.get_next(), end=' ')
print()

rng = MyRange(5,10,2)

while rng.has_next():
    print(rng.get_next(), end=' ')
