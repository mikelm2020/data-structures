class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __random_fill__(self):
        import random

        for i in range(len(self.items)):
            self.items[i] = random.randint(i + 1, len(self.items))

    def __secuence_fill__(self):
        for i in range(len(self.items)):
            self.items[i] = i + 1

    def __custom_sum__(self):
        from functools import reduce

        return reduce(lambda a, b: a + b, self.items)
