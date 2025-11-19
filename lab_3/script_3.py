class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


iterator_1 = Iterator("abc")

print("Использование итератора для строки:")
for elem in iterator_1:
    print(elem)

iterator_2 = Iterator([1, 2, 3])

print("Использование итератора для списка:")
for elem in iterator_2:
    print(elem)
