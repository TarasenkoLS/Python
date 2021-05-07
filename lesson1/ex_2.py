sec = int(input('Введите время в секундах: '))
hour = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60
# print("%02d:%02d:%02d" % (hour, min, sec))
print("{:02d}:" "{:02d}:" "{:02d}".format(hour, min, sec))
