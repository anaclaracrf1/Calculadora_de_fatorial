while True:
    print('\033[36m=\033[m'*40)
    n =int(input('Você deseja ver a tabuada de que número?'))
    print('\033[36m=\033[m'*40 )
    if n< 0 :
        break
    else:
        for i in range(1,11):
            print(f'{n} X {i} = {n*i}')