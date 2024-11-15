sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3
}

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    assert expected_args is not None
    assert len(size) == expected_args
    assert all(s >= 0 for s in size)
    
    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a

    result = eval(f'{fig}.{func}(*{size})')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:n")

    while len(size) != sizes.get(f"{fig}-{func}", 1):
        size = list(map(int, input(
            "Input figure sizes separated by space, 1 for circle and squaren"
        ).split(' ')))

    result = calc(fig, func, size)
    print(f'Result: {result}')
