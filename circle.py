import math


def area(r):
    '''Принимает число r (радиус) и возвращает площадь круга по формуле S = πr^2
    
        Параметры:
            r (int): десятичное целое число

        Возвращаемое значение:
            area_result (int) : целое число r во второй степени, умноженное на число π

        Пример вызова:
            print(area(2))
            > 12.566370614359172
    '''
    area_result = math.pi * r * r
    return area_result


def circumference(r):
    '''Принимает число r (радиус) и возвращает периметр круга по формуле C = 2πr
    
        Параметры:
            r (int): десятичное целое число

        Возвращаемое значение:
            circumference_result (int) : удвоенное произведение целого числа r, умноженного на число π

        Пример вызова:
            print(circumference(3))
            > 18.84955592153876
    '''
    circumference_result = 2 * math.pi * r
    return circumference_result

