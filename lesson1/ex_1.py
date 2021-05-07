bon = int(input('Введите год своего рождения: '))
year = 2021
print('В', year, 'году Вам исполнится ', year - bon, 'лет.')
height = float(input('Введите ваш рост в м: '))
weight = float(input('Введите ваш вес в кг: '))
i = weight / (height ** 2)
print(f"Индекс массы вашего тела - {i:.2f}")