'''
Created on 15/08/2024

@author: jsuarezd
'''
# las variables no nesesitan ser inicializadas, pueden adquirir cualquier tipo de dato
nombre1="juan"
nombre2=1234
print(nombre1+" "+str(nombre2))
# tambien se puede cambiar el valor de la variable
nombre2="12345"
print(nombre1+" "+nombre2)
# tambien se pueden sumar dos variables
numero1=1
numero2=3
print(numero1+numero2)
# puedo tambien guardar un input dentro de una variable y hacer operaciones con ellas
numero1=int(input("digita el numero 1 : "))
numero2=int(input("digita el numero 2 : "))
print(numero1+numero2)
# las variables pueden cambiar, si nesesitamos saber que tipo de variable es podemos utilizar type
numero="hola soy string"
print(numero)
print(type(numero))
numero=1
print(numero)
print(type(numero))
# puedo tambien hacer operaciones con una misma variable
numero=1
print(numero+numero+2)
#puedo sumar tambien floats y enteros dentro de una variable
numeo=5+5.8
print(numeo)
print(type(numeo))
#conversiones inplicitas
#las conversiones implicitas son aquellas que no nesesitan que nosotros metamos mano
#en este ejemplo num1 primero es entero y luego se convierte en un float
num=1
print("antes de la  canversion num es igual a : "+str(num) +" y es un")
print(type(num))
num=num+5.8
print("le sumamos a num 5.8 : "+str(num) +"  y ahora es")
print(type(num))
#ahora las conversiones explicitas son las que hacemos manualmente
num=1
print("antes de la  canversion num es igual a : "+str(num) +" y es un")
print(type(num))
num=str(num)
print("cambiamos con str la clase de num "+str(num) +"  y ahora es")
print(type(num))
#formatear cadenas
#forma larga con conversion
x=1
y=2
print("forma antigua con conversion str valor de x : "+str(x)+" valor de y : "+str(y))
#forma con funcion antigua 2
print("forma con funcion antogua 2 valor de x es : {} y el valor de y es : {}".format(x,y))
#puedo hacer operaciones tambien
print("valor de x : {}  valor de y es : {} y sumados los dos {}".format(x,y,x+y))
# la nueva manere de hacer con f es de la siguiente forma
color="rojo"
matricula=2222
print(f"la nueva manera el color tiene el valor de {color} y la matricula tiene el valor de {matricula}")
