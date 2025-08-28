#ejercicio1
print("hola mundo")
#ejercicio2
nombre=input("ingresa tu nombre")
print(f"hola",nombre)
#ejercicio3
nombre=input("ingrese su nombre")
apellido=input("dime tu apellido")
edad=int(input("dime tu edad"))
lugar_de_residencia=input("dime donde vives")
print(f"soy {nombre}{apellido}, tengo {edad} años, y vivo en {lugar_de_residencia}")
#ejecicio4
import math
radio=float (input("ingrese el radio"))
area= math.pi * radio **2
perimetro=2*math.pi*radio
print (f"El area del circulo es:{area} y el perimetro es:{perimetro}")
#ejercicio5
segundos=int(input ("ingrese la cantidad de segundos"))
horas=segundos//3600
print(f"la cantidad de horas ingresadas en segundos son:{horas}")
#ejercicio6
numero=int(input("ingrese un numero"))
print(numero *1)
print(numero*2)
print(numero*3)
print(numero*4)
print(numero*5)
print(numero*6)
print(numero*7)
print(numero*8)
print(numero*9)
print(numero*10)
#ejercicio7
numero1=int(input("ingrese un primer numero mayor que 0"))
numero2=int(input("ingrese un segundo numero mayor que 0"))
suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
print(f"la suma es:{suma}, la resta es: {resta}, la multiplicacion es {multiplicacion}, y la division es:{division} ")
#ejercicio8
altura=float(input("ingrese tu altura"))
peso=float(input("ingrese su peso"))
masa_corporal=peso / altura**2
print(f"la masa corporal es:{masa_corporal}")
#ejercicio9
grados_c=float(input("ingrese la temperatura en grados celsius"))
grados_f=9/5*grados_c+32
print(f"los grados en fahrenheit son:{grados_f}")
#ejercicio10
num1=int(input("ingrese el primer numero"))
num2=int(input("ingrese el segundo numero"))
num3=int(input("ingrese el tercer numero"))
promedio=(num1+num2+num3)/3
print("el promedio es",promedio)