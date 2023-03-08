import math
co = float(input('Comprimento do cateto oposto em metros:'))
ca = float(input('Comprimento do cateto adjacente em metros:'))
h = math.sqrt(co*ca)
print(f'O comprimento da hiotenusa é de {h} metros')