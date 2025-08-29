#Practica 1 estructuras secuenciales
#Nahuel Lemus

import math
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")
#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre=input("ingrese su nombre:")
print(f"Bienvenido, {nombre}!")
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre=input("ingrese su nombre:")
apellido=input("ingrese su apellido:")
edad=input("ingrese su edad:")
lugar=input("ingrese su lugar de residencia:")
print(f"Eres {nombre} {apellido}, tienes {edad} años y vives en {lugar}")
# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio=float(input("Ingrese el radio del circulo:"))
area=(radio**2)*math.pi
perimetro=2*radio*math.pi   
print(f"El perímetro es de {perimetro}cm y el área es de {area}cm.")
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos=int(input("Ingrese cantidad de segundos:"))
horas=segundos/3600
print(f"{segundos} segundos equivalen a {horas} horas.")
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
mult=int(input("Ingrese un número:"))
mult2 = 2 * mult
mult3 = 3 * mult
mult4 = 4 * mult
mult5 = 5 * mult
mult6 = 6 * mult
mult7 = 7 * mult
mult8 = 8 * mult
mult9 = 9 * mult
mult10 = 10 * mult
print(f"""La tabla del {mult} es: 
 {mult} * 1 = {mult}
 {mult} * 2 = {mult2}
 {mult} * 3 = {mult3}
 {mult} * 4 = {mult4}
 {mult} * 5 = {mult5}
 {mult} * 6 = {mult6}
 {mult} * 7 = {mult7}
 {mult} * 8 = {mult8}
 {mult} * 9 = {mult9}
 {mult} * 10 = {mult10}
""")
# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1=int(input("Ingrese un entero distinto a cero:"))
num2=int(input("Ingrese un segundo entero distinto a cero:"))
suma=num1+num2
resta=num1-num2
division=num1/num2
multiplicacion=num1*num2
print(f"""
      {num1} + {num2} = {suma}
      {num1} - {num2} = {resta}
      {num1} * {num2} = {multiplicacion}
      {num1} / {num2} = {division}
""")
# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
masa=float(input("Ingrese su peso en kg:"))
altura=float(input("Ingrese su altura en cm:"))
imc=masa/((altura/100)**2)
print(f"Su indice de masa corporal es de: {imc}")
# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
celsius=float(input("Ingrese temperatura en celcius (°C):"))
farenheit=(9/5)*celsius + 32
print(f"{celsius}°C equivalen a {farenheit}°F.")
# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num1=float(input("Ingrese un primer número:"))
num2=float(input("Ingrese un segundo número:"))
num3=float(input("Ingrese un tercer número:"))
promedio= (num1+num2+num3)/3
print(f"El promedio de los 3 números es: {promedio}")

#Practica 1 estructuras secuenciales
#Nahuel Lemus
