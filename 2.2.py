place = int(input("enter sit numder: "))
a = ''
if place % 6 == 5 or place % 6 == 0:
    a += 'боковое '
else: 
    a += 'купе '
if place % 2 == 0:
    a += 'верхнее '
else: 
    a += 'нижнее '
print('Ваше место ', place , a)