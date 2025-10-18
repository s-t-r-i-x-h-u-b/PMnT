def nod (a, b):
    if a < b:
        temp = a
        a = b
        b = temp
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        temp = b
        b = a % b
        a = temp
    

print ("Введите первое число: ")
a = int(input())
print ("Введите второе число: ")
b = int(input())
print ("Наибольший общий делитель:", nod(a,b))
