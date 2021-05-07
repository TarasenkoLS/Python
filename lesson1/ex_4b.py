number = int(input("Введите целое положительное число: "))
max_n = 0
num = number
while num > 0:
    if max_n < num % 10:
        max_n = num % 10
    num = num // 10
print(max_n, "- максимальная цифра в введеном числе", number)

