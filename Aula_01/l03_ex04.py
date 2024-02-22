import math 

print("Digite a base e a altura do retângulo: ")
base = int(input())
altura = int(input())

area = (base * altura)
perimetro = ((base * 2) + (altura * 2))
diagonal =  math.sqrt((perimetro**2) - (8 * area))
diagonal = diagonal * 0.5
print(area, perimetro, diagonal)