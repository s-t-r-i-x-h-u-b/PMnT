def natural_number_input():
    print("Введите число")
    n = int(input())
    while n < 1:
        print("Число должно быть положительным")
        n = int(input())
    return n


n = natural_number_input()
d = {x: x**2 for x in range(n + 1)}
for key, value in d.items():
    print(key, value)