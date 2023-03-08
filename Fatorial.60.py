import math
print('Calcule o \033[34mFATORIAL:\033[m')
n = int(input('Você deseja saber o fatorial de que número?'))
f = n
ft = math.factorial(n)
print(f'O fatorial de \033[34m{n}! = ', end='')
while f > 0:
    print(f'{f}', end='')
    print('.' if f >1 else ' =', end='')
    f -= 1
print(f' {ft}',end = '')
