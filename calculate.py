import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
        # Возвращает значение заданной функции для указанной фигуры на основе её размеров

        # Параметры:
                # func (str): название функции (perimeter или area)
                # fig (str): название фигуры (circle или square)
                # size (list): список размеров фигуры (для круга - радиус, для квадрата - сторона)

        # Возвращаемое значение
                # (float): результат вычисления функции для указанной фигуры
                
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



