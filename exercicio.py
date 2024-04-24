import math
print("☆·˚｡•  calculadora de equação de segundo grau  •｡˚·☆")
a = float(input ("Digite o 1° valor: "))
if a == 0:
  print ("Em equações de segundo grau o valor de 'a' não pode ser 0. Digite outro valor!")
  a = float(input ("Digite o 1° valor: "))
b = float(input("Digite o 2° valor: "))
c = float(input("Digite o 3° valor: "))
delta= ((b) ** 2) - 4 * a * c
if delta < 0:
    print ("Essa equação possui raízes complexas, desculpe, não sou capaz de calcular :(")
else:
    raiz= math.sqrt(delta)
    x1= (-b + raiz) / (2 * a)
    x2= (-b - raiz) / (2 * a)
    if delta == 0:
       print ("Essa equação possui apenas uma raíz real, que é", x1)
    else:
        print ("Essa equação possui duas raízes reais e distintas, e os valor de x¹ é", x1, "e o de x² é", x2 )