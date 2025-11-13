def sum_odd_numbers(n):
    sum = 0
    for i in range(n + 1):
      if i % 2:
        sum += i
    return sum

def natural_number_input():
    print("Введите число")
    n = int(input())
    while n < 1:
      print("Число должно быть положительным")
      n = int(input())
    return n


n = natural_number_input()
print(f"Сумма всех нечётных чисел до {n} = {sum_odd_numbers(n)}")