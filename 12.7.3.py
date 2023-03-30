money = float(int(input("Введите сумму вклада   ")))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(per_cent.values())
deposit_max = int(max(list(map(lambda x: x*money/100.0, deposit))))
#print("money =", int(money))
#print("deposit =", deposit )
print("Максимальная сумма, которую вы можете заработать", deposit_max)


1