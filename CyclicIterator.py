
class CyclicIterator:
    def __init__(self, value):
        self.value = list(value)
        self.stop_value = value.stop - 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > self.stop_value:
            self.index = 0
        return self.value[self.index]


cyclic_iterator = CyclicIterator(range(6))
for i in cyclic_iterator:
    print(i)
