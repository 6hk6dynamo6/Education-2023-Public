count = int(input("Введите количество билетов, которое хотите приобрести    "))
#Запрашиваем у пользователя "Сколько Вам билетов?"
sum = 0.0
#Считаем общую сумму билетов за цикл покупки, начинаем со значения 0

for i in range(1, count + 1):
    age = int(input("Введите возраст посетителя   "))
    if 18 < age <= 25:
        sum = sum + 990.0
    elif 25 < age:
        sum = sum + 1390.0
    print("Сумма до скидки", sum)
    #можно выводить сумму после каждой итерации для проверки работоспособности программы
if 3 < count:
#проверяем сколько билетов регистрируется, вычисляем сумму после скидки
    sum = sum - sum * 10.0/100.0
print("Сумма после скидки", sum)
#Выводим итоговую стоимость билетов