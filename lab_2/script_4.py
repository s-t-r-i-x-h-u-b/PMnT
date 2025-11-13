def fibonacci(n):
    l = []
    a = 0
    l.append(a)
    if n == 1:
        return l
    b = 1
    l.append(b)
    if n == 2:
        return l
    n -= 2
    while n > 0:
        temp = b
        b += a
        a = temp
        l.append(b)
        n -= 1
    return l

def natural_number_input():
    print("Введите число")
    n = int(input())
    while n < 1:
        print("Число должно быть положительным")
        n = int(input())
    return n


n = natural_number_input()
print(fibonacci(n))