def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

num = int(input())
print ("Рекурсивная сумма:", sum(num))
