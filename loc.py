import locale
 
locale.setlocale(locale.LC_ALL, "ru")   
 
money = 123456789.99
formatted = locale.currency(money)
print(formatted)   
