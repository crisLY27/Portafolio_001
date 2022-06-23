"""
UNIVERSIDAD NACIONAL DE SAN AGUSTIN
ESCUELA PROFECIONAL DE INGENIERÌA EN TELECOMUNICACIONES
ALUMNO: LARICO YUCRA, CRISTHIAN DENIS
PRACTICA 2
"""
#VARIABLES Y TIPOS DE DATOS
x= 5            
y= 5.5          
j="q"           
k="Buenos Dias" 
m=True          
type(x)
type(y)
type(j) 
type(m)
print(type(x))


#OPERADORES ARITMETICOS

15 / 6
15 // 6
15%6
a=27
b=6

print (a/b)
print(a//b)
print(a%b)

#ORDEN DE OPERADORES

-3 + 4 ** 2 * 10/5 
(-3 + 4) ** 2 * 10/5 
a = 6
b=9.5
resultado = (a*b)//2
print(resultado)
print(type(resultado))

#OPERACIONALES RELACIONALES

10 > 50
x = 100
y = 14

x==y

print(x==y)

#OPERADORES LOGICOS

def imprime_3():
    print("Buenos Dias")
    print("Buenos Dias")
    print("Buenos Dias")
    
imprime_3()


def imprime_3():
    print(" Buenos Dias \n" *3 )
    
imprime_3()

def imprime_3 (a):
    print(a*10)
x = "Hola mundo \n"
imprime_3(x)

def area_cuadrado(lado):
    area = lado **2
    return(area)
print (area_cuadrado(6))

import math

pi = math.pi
print(pi)


#EJEMPLOS EN JUPYTER NOTEBOOK


x = "Bienvenidos a Phyton"
y = 'en minusculas'


lowcase = x.lower()         
uppcase = x.upper()         
titcase = y.title()         

print('\n',lowcase)
print('\n',uppcase)
print('\n',titcase)
          

x = "Bienvenidos a Phyton"
y = 'en minusculas'


lowcase = x.lower()       
uppcase = x.upper()        
titcase = y.title()       

print('\t',lowcase,'\t',uppcase,'\t',titcase)   


nom ="milo"
age =25
print("Hola,\n Me llamo: ", nom, "\n y tengo: ",age, "años")


x= 10 *3.25
y=200 * 200

z= 'el valor de "x" es : ' +   repr (x) + ', y el valor de "y" es' + repr (y) +'...'

print(z)
print ('el valor de "x" es: ',x,', y el valor de "y" es ',y,' ... ')

#FORMATEAR CADENAS

import math

print (f'el valor de "pi" es proximadamente: {math.pi:3f}')


nom = "Milo"
age = 25


print(f"hola,\n Me llamo: {nom} \n y tengo: {age} años. ")

nom= "Milo"
age = 25

print("Hola,\n Me llamo: {0} \n y tengo {1} años.".format(nom,age))

print ("Ingrese su Nombre")
nom = input()

# Funcion Input( )

print(f"un gusto conocerte , {nom}")

nom = input("ingrese su nombre: ")

print(f"Un gusto conocerte , {nom}")

#FUNCIONES

def valor(precio):
    igv = precio * 0.18
    importe=precio + igv
    return(importe)
producto = input('ingrese nombre del producto: ')
importe = input("ingrese el precio del producto: ")


print('el importe total de {0}, es : {1}'.format(producto,valor(importe)))

def valor(precio):
    igv = precio * 0.18
    importe=precio + igv
    return(importe)


producto = input('Ingrese nombre del Producto: ')
imp = float(input("Ingrese el Precio del Producto:"))

print('El importe total de {0}, es: {1}'.format(producto,valor(imp)))

#PRACTICA TERMINADA



