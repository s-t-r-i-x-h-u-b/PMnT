list = []
print ("Чтобы закончить введите 0")
while True:
    print ("Введите элемент списка: ")
    c = int(input())
    if (c == 0): break
    list.append(c)
min = list[0]
for i in list:
    if i < min:
        min = i
print ("Минимальный элемент списка:", min)
