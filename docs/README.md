# Документация проекта

## Общее описание решения
Данный проект предназначен для вычисления площади и периметра квадрата и круга, периметра и полупериметра треугольника, а также для вычисления значения заданной функции для указанной фигуры на основе её размеров. Он предоставляет простые функции, которые можно использовать для получения необходимых значений, используя переданные параметры.

## Функции

### Квадрат

#### Функция area(a)
def area(a):
    """
    Возвращает площадь квадрата по длине его стороны (a)

        Параметры:
            a (float): длина стороны квадрата

        Возвращаемое значение:
            (float): площадь квадрата
            
    Пример вызова:
    >>> area(4)
    16.0
    >>> area(2.5)
    6.25
	"""
    return a * a

#### Функция perimeter(a)
def perimeter(a):
    """
    Возвращает периметр квадрата по длине его стороны (a)

        Параметры:
		     a (float): длина стороны квадрата

        Возвращаемое значение:
            (float): периметр квадрата
    
    Пример вызова:
    >>> perimeter(4)
    16.0
    >>> perimeter(2.5)
    10.0
    """
    return 4 * a


### Круг

#### Функция area(r)
import math
def area(r):
    """
    Возвращает площадь круга по длине его радиуса (r)
    
        Параметры:
            r (float): длина радиуса круга

        Возвращаемое значение:
            (float): площадь круга
            
    Пример вызова:
    >>> area(3)
    28.274333882308138
    >>> area(1)
    3.141592653589793
    """
    return math.pi * r * r

#### Функция perimeter(r)
def perimeter(r):
    Возвращает периметр круга (длину окружности) по длине его радиуса (r)
    
        Параметры:
            r (float): длина радиуса круга

        Возвращаемое значение:
            (float): периметр круга (длина окружности)
    
    Пример вызова:
    >>> perimeter(3)
    18.84955592153876
    >>> perimeter(1)
    6.283185307179586
    """
    return 2 * math.pi * r

### Треугольник

#### Функция area(a, b, c)
def area(a, b, c):
    Возвращает полупериметр треугольника по длинам его сторон (a, b, c)

        Параметры:
            a (float): длина первой стороны треугольника
            b (float): длина второй стороны треугольника
            c (float): длина третьей стороны треугольника

        Возвращаемое значение:
            (float): полупериметр треугольника
            
    Пример вызова:
    >>> area(3.0, 4.0, 5.0)
    6.0
    >>> area(6.5, 7.2, 8.3)
    11.0
    """
    return (a + b + c) / 2
    
#### Функция perimeter(a, b, c)
def perimeter(a, b, c):
    Возвращает периметр треугольника по длинам его сторон (a, b, c)

        Параметры:
            a (float): длина первой стороны треугольника
            b (float): длина второй стороны треугольника
            c (float): длина третьей стороны треугольника

        Возвращаемое значение:
            (float): периметр треугольника
            
	Пример вызова:
    >>> perimeter(3.0, 4.0, 5.0)
	12.0
	>>> perimeter(6.5, 7.2, 8.3)
	22.0
    """
    return a + b + c

### Калькулятор
import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

#### Функция calc(fig, func, size)
def calc(fig, func, size):
    Возвращает значение заданной функции для указанной фигуры на основе её размеров

        Параметры:
                func (str): название функции (perimeter или area)
                fig (str): название фигуры (circle или square)
                size (list): список размеров фигуры (для круга - радиус, для квадрата - сторона)

        Возвращаемое значение
                (float): результат вычисления функции для указанной фигуры
                
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
	
	Пример вызова:
    >>> # для круга
    >>> # если radius = 5
    >>> calc('circle', 'perimeter', [5])
    perimeter of circle is 31.4159

    >>> # для квадрата
    >>> # если side = 4
    >>> calc('square', 'area', [4])
    area of square is 16

## История изменений проекта с хэшами коммитов (кроме последней записи)
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added

