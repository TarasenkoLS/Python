number = int(input("Введите целое положительное число: "))
count = len(str(number))
max_n = 0
while count > 0:
    if max_n < number % 10:
        max_n = number % 10
    number = number // 10
    count = count - 1
print("Максимальная цифра в введеном числе: ", max_n)
