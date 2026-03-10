#programa calculadora com IF-ELIF-ELSE
# 10/03/2026

jv = input("Digite 1-SOMA ou 2-SUBTRAÇAO ou 3-MULTIPLICAÇAO ou 4-DIVISAO ou 5-POTENCIAÇAO ou 6-RADICIAÇAO")
jv = int(jv)

a = input("Entre com 1° número")
a = int(a)

b = input(" entre com o 2° número")
b = int(b)

if (jv == 1):
      print(a + b)
elif (jv == 2):
    print(a - b)
    
elif (jv == 3):
    print(a * b)
    
elif (jv == 4):
    print(a / b)
    
elif (jv == 5):
    print(a ** b)
    
elif (jv == 6):
    print(a ** (1/2))

else:
    print("digite uma opçao valida")
input()  


