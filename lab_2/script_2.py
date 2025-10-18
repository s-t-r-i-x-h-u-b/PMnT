while True:
    print("Выберите действие: +, -, *, /")
    c = input()
    if (c == '+' or c == '-' or c == '*' or c == '/'):
        break;

print("Введите первое число: ")
a = float(input())
print("Введите второе число: ")
b = float(input())

if c == '+':
    print (a + b)
elif c == '-':
    print (a - b)
elif c == '*':
    print (a * b)
elif c == '/':
    print (a / b)
