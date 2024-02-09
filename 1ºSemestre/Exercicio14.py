import math

cateto1 = int(input("Digite o primeiro cateto: "))

cateto2 = int(input("Digite o segundo cateto: "))

somaCatetos = (cateto1 ** 2) +  (cateto2 ** 2)

hipotenusa = math.sqrt(somaCatetos)

print("a Hipotenusa desse triângulo é: ", hipotenusa)
