color = str(input('Введите цвета: '))
if color != 'красный' and color !='синий' and color != 'желтый':
    print('error')
else:
    color2 = str(input('Введите цвета 2: '))
    if color2 != 'красный' and color2 !='синий' and color2 != 'желтый':
        print('error')
    else:
        if (color == 'красный' and color2 == 'синий') or (color == 'синий' and color2 == 'красный'):
            print('фиолетовый')
        elif (color == 'красный' and color2 == 'желтый') or (color == 'желтый' and color2 == 'красный'):
            print('оранжевый')
        elif (color == 'синий' and color2 == 'желтый') or (color == 'желтый' and color2 == 'синий'):
            print('зеленый')

