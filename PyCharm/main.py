money = input('Введите сумму:')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = per_cent['ТКБ']
b = per_cent['СКБ']
c = per_cent['ВТБ']
d = per_cent['СБЕР']
deposit = (a * int(money)*0.01,b * int(money)*0.01, c * int(money)*0.01, d * int(money)*0.01)
i = max(deposit)
print ('deposit = ', list(deposit))
print ('Максимальная сумма, которую вы можете заработать —', i)