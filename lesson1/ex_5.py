rev = int(input("Введите сумму выручки: "))
cost = int(input("Введите сумму издержек: "))
profit = rev - cost
if profit > 0:
    print("Ваша прибыль составила ", profit)
    print(f"Рентабельность составила {(profit / rev):.0%}")
    staff = int(input("Введите количесво сотрудников фирмы: "))
    print("Прибыль фирмы в расчете на одного сотрудника составляет ", profit / staff)
elif profit < 0:
    print("Ваш убыток составил ", profit * (-1))
else:
    print("Ваша фирма сработала в 0")
