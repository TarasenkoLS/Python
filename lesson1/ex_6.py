start = int(input("Введите длину текущей дистанции: "))
fin = int(input("Введите длину желаемой дистанции: "))
day = 1
print(day, "-й день: ", start)
while start <= fin:
    start = start * 1.1
    day += 1
    print(day, "-й день: {:.2f}".format(start))
print("Вы достигните цели на", day, "-й день тренировок")
