#trabajo practico numero 3
#ejercicio1

edad=int(input("ingrese su edad"))
if edad >= 18:
    print("es mayor de edad")
print("su edad fue verificada")   

#ejercicio2

nota=int(input("ingrese su nota"))
if nota >= 6:
    print("aprobado")
else:
    print("Desaprobado")

#ejercicio3

num=int(input("ingrese un numero, que sea par"))
if num % 2 == 0:
    print("el numero ingresado es par")
else:
    print("por favor, ingrese un numero par")     

#ejercicio4

edat=int(input("ingrese su edad"))
if edat < 12:
    print("categoria niño/a")
elif edat >= 12 and edat < 18:
    print("categoria adolescente")
elif edat >= 18 and edat < 30:
    print("Categoria adulto joven")             
elif edat >= 30: 
    print("categoria adulto/a")    

#ejercicio5

contrasena=input("ingrese una contraseña de 8 a 14 caracteres en numeros")
if len(contrasena)>=8 and len(contrasena)<=14:
    print("contraseña valida")
else:
    print("Contraseña invalida. Por favor ingrese una contraseña entre 8y14 caracteres")

#ejercicio6

import random
numeros_aleatorios= [random.randint(1, 100) for i in range(10)]
from statistics import mode, median, mean
media=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
moda=mode(numeros_aleatorios)
#mostrar por pantallas los valores
print("numeros:", numeros_aleatorios)
print("la mediana es", mediana)
print("la moda es:", moda)
print("la media es:", media)
if media> mediana and mediana > moda:
    print("el sesgo es positivo")
elif media < mediana and mediana < moda:
    print("el sesgo es negativo")
elif moda==mediana==media:
    print("no hay sesgo") 
else:
    print("la distribucion no representa un sesgo claro(APROX. SIMETRICO)")           

#ejercicio7

frase=input("ingrese una frase o palabra")
if frase and frase [-1].lower()in 'aeiou' or 'AEIOU':
    print(frase,"!")
else:
    print(frase)    

#ejercicio8

nombre=input("ingrese su nombre")
opcion=int(input("ingrese 1 si quiere su nombre en mayusculas, 2 si quiere su nombre en minusculas, y 3 si quiere su nombre con la primer letra mayuscula"))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#ejercicio9

magnitud=float(input("ingrese la magnitud del terremoto"))
if magnitud== 3:
    print ("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print ("leve(ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("moderado(sentido por personas pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("fuerte(puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud <7:
    print ("muy fuerte(puede causar daños significativos)")
elif magnitud >= 7:
    print ("extreme(puede causar graves daños a gran escala)")

#ejercicio10

hemisferio=input("ingrese en que hemisferio se encuentra (N/S)")
mes=int(input("ingrese que mes del año es"))
dia=int(input("ingrese que dia es"))
if (dia >= 21 and mes== 12) or ( mes in(1,2))or (mes==3 and dia<=20):
    if hemisferio == 'norte':
        print("invierno")
    else:
        print("verano")    

