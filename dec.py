from decimal import *

getcontext().prec = 30

x = Decimal(1)
y = Decimal(7)

result = x / y

print("деление 1 на 7 с точностью до 30 знаков после запятой:", result)

