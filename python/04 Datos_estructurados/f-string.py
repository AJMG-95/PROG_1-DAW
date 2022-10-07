for i in range(1, 11):
    print(f'{"*"*i:>10}')

for i in range(1, 11):
    print(f'{"*"*i:<10}')

for i in range(1, 11, 2):
    print(f'{"*"*i:^10}')


def arbolito(n):
    for i in range(1, n * 2 - 1, 2):
        print(f'{"*"*i:^10}')
    x = '*'.center(n * 2 - 1)
    print(f'{x}')
