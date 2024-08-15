'''
Created on 15/08/2024

@author: jsuarezd
'''
#input para ingresar informacion
input("dime tu nombre : ")
#orden de ejecucion primero el input y despues el print
print(input("dime tu nombre : "))
#orden de ejecucion primero el input y despues el print concatenado con string
print("tu nombre es  : "+input("dime tu nombre : "))
#inputs concatenado con los string del print
print("tu nombre es  : "+input("dime tu nombre : ")+" "+input("dime tu apellido : "))
#inputs mejorado para una mejor comprension lectura de codigo
print("tu nombre es  : "+(input("dime tu nombre : "))+" "+(input("dime tu apellido : ")))
