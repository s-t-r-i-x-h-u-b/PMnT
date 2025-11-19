class Counter:
    def __init__(self, value=0):
        self.__value = value

    def __iadd__(self, value):
        self.__value += value
        return self

    def __isub__(self, value):
        self.__value -= value
        return self

    @property
    def value(self):
        return self.__value


counter = Counter()
print(counter.value)
counter += 1
print(counter.value)
counter -= 1
print(counter.value)
