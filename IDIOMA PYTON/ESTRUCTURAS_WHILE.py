"""
UNIVERSIDAD NACIONAL DE SAN AGUSTIN
ESCUELA PROFECIONAL DE INGENIERÌA EN TELECOMUNICACIONES
ALUMNO: LARICO YUCRA, CRISTHIAN DENIS
PRACTICA 5
"""

#DESARROLLO

# ESTRUCTURA INTERACTIVA - BUBLE WHILE

# hacer un programa que imprima la tabla del 3

contador =0
print("tabla del numero 3")

while contador <=10:
    print(f"3 x {contador} ==> {contador * 3 }")
    contador  += 1
print ("fin de la tabla")

# Hacer un programa que repita frase las veces que desee use funciones.
frase = "nunca te rindas en todos los proyectos, y recuerda la inteligencia no es igual a la sabiduria **TIENES QUE SER SABIO**"

cont=0

def repetir(n,cont):
    while cont < n :
        print(frase)
        cont +=1
num=int(input("ingrese el numero de veces a repetir la frase: "))
print("\n\n")
repetir(num,cont)


# HACER UN PROGRAMA QUE SOLICITE INGRESO DE CONTRASEÑA


password =""

while password !="SOY EL MEJOR ALUMNO DE COMPUTACION EN EL GRUPOC":
    print("porfavor ingrese su contraseña")
    password =input()
print("usted ingreso bien su contraseña TOMA TU CARAMELITO")


# MODIFICANDO LA FINALIZACION DEL BUCLE WHILE: BREAK Y CONTINUE


###  USO DE BREAK:
###  HACER UN PROGRAMA QUE VALIDE INGRESO NOMBRE ROSE:
    
    
while True:
    print("porfavor ingrese su nombre: ")
    name  = input ()
    if name.lower() == "rose":
        break
print("el nombre es valido :rose es un bonito nombre ")  

nombre=["alexander","rudy","yordan","cristhian","cesar","manuel","el profesor","mi mama"]
contra=["123456","654321","soyguapo","987654","254766","950819015","900853357","amo a mim perro","me gusta el curso de computacion2"]

while True:
    name=input("ingrese su nombre: " )
    if name not in nombre:
        continue
    print(f"\n hola  {name.title()},por favor ingrese su contraseña:")
    password =input()
    if password in contra:
        print("\n Bienvenido a su cuenta Bancaria")
        break
    else:
        print("\n Acceso Denegado ************* *****estafador****** **********")
        break

# "se viene lo mejor que son los ejemplos :D "   
# ********************************** EJEMPLOS*******************

# Hacer un programa que solicite iongreso de contraseña con intentos limitados:
password =""

cont=0
while password !="12345":
    cont +=1
    print("porfavor ingrese su contraseña: ")
    password =input()
    if cont==5:
        print("finalizo los intentos....!!!!!************** error syntax")
        break
if cont!=5:
    print ("alfin te acordaste, pense que no te acordabas de tu contraseña , para la siguiente no  seas tan distraido ")  
    
    
# imprime la secuencia 3n+1 desde un numero n, terminando cuando llegue a 1.


def seq3np1(n):
    while n!= 1:
        print(n,end=", ")
        if n% 2 == 0:
            n=n//2
        else:
            n=n*3+1
    print(n,end =".\n")

num =int(input("Ingrese numero de inicio n :  ==> "))
seq3np1(num)    
 
    
# Hacer un programa con funcion que cuenta el numero de digitos que son 1 o 5 en un numero entero positivo:
def num_digi (n) :
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0  or digit == 5:
            count = count + 1
        n = n // 10
    return count
num =int(input("ingrese un numero que contenga los digitos *** 0 *** y *** 5 *** : ==> "))

cantidad=num_digi(num)

print ("\n\n\tLa cantidad de digitos ***0*** y ***5*** en el numero ",num,"es: ==> ",cantidad)
    
    
    
#******************************GRACIAS TOTALES *************************
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    