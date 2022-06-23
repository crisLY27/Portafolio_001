"""
UNIVERSIDAD NACIONAL DE SAN AGUSTIN
ESCUELA PROFECIONAL DE INGENIERÌA EN TELECOMUNICACIONES
ALUMNO: LARICO YUCRA, CRISTHIAN DENIS
PRACTICA 3
"""
# 1.- Introduccion a Lista
cadena= "si quieres aprender, enseña. Marco Tulio Ciceron"    

print("La frase inicia con la letra:",cadena[0])        
print ("La frase termine con la letra: ",cadena[-6])


lista_de_cadena=cadena.split() 
print(lista_de_cadena)  


lista_de_nombres = ["luis","pablo","mili","gabriela","oscar"] 
print(lista_de_nombres)

lista_numeros=[20, 30, 40, 50, 60]
print(lista_numeros)


print(lista_numeros[0])          
print (lista_numeros[-1]*5)    
print (lista_numeros[2])

print("\n")
print(lista_de_nombres)
print(lista_de_nombres[0].title())
print(lista_de_nombres[-1].upper())
print(lista_de_nombres[2])
### Modificando elementos en una lista, porque la lista es mutable:

celulares= ["iphone","sansung","huavei", "motorola" , "xiaomi"]
print(celulares)

celulares[1]="samsung"  
celulares[2]= "huawey" 

print (celulares)

celulares= ["iphone","samsung","huawei","motorola","xiaomi"]
celulares.append("lg")   
print(celulares)

cel= ["zte", "logic"]  
cel2= celulares+cel        
print(cel2) 

### Borrando elementos de una lista

celulares= ['iphone', 'samsung', 'huawei', 'motorola', 'xiaomi', 'lg', 'zte', 'logic']

print("\nlista de celulares originales")
print (celulares)

del celulares[-1]   
print("\nLista con el ultimo celular borrado")
print(celulares)
        
b_celular = celulares.pop(4)  
print("\nLista borrando el celular nuevamente")
print(celulares)
print("\nEquipo Celulares Borrado")
print(b_celular.upper())


c_celular= "lg"                
celulares.remove(c_celular)
print(f"\nLista borrando celular {c_celular.upper()}")
print(celulares)
print(f"\nEl celular {c_celular.upper()} es muy malo para mi") 

# Ordenamos una lista
 
autos = ["mazda","audi","toyota","subaru","bmw","lamborghini"]
print("\nLista Original")
print(autos)

print("\nLista Ordenada")
autos.sort()   
print(autos)

print("\nLista Ordenada a la Inversa")
autos.reverse()        
print(autos)


num = [200, 600, 10, 2000, -5, 50, 110, 1500]
print("\nLista Original" )
print(num)


print("\nlista ordenada Temporal")
print(sorted(num))   

print("\nLista Original de nuevo")
print(num)
#*********************************ESTRUCTURAS CONDICIONALES****************************************

# CONDICIONALES SIMPLES:
x = "Guido"
print("i" in x)
print("i" not in x)


lista = ["unva","naranja","pera","manzanas"]

print("uva" in lista)

x=100
y=200
print(x, "es iguala", y, " ===>> ", x==y)


print("1 < 7 = ", 1>7)       
print("2 < 9 = ", 2>=9)    
print("10 == 20 = ", 10==20) 
print("escuela == casa =" ,"escuela"=="casa")   
print("python != Java = " , "python" != "Java")


x=20

if x> 0 :                                   
    print("el numero ",x,"es valido")
    print("el cuadrado del numero ",x,"es :" ,x*x)
    
# Comando if-else condicional

n = 15
m = 20

if n>m:
    print("El numero MAYOR es:" +str(n))
else:
    print("el numero MAYOR es: " +str(m))
    

a = int(input("ingrese el primer Numero:"))
b = int(input("ingrese el primer Numero:"))
c = int(input("ingrese el primer Numero:"))      

if a> b:
    if a>c:
        m=a
    else:
        m = c
else:
    if b > c:
        m = b
    else:
            m = c
            
print("El numero MAYOR es:  "+str(m)) 
print("El numero MAYOR es: {}".format(m))
# Comando if-elif-else-Condicional encadenado


nombre = input("Ingrese su Nombre: ")
if"a" in nombre:
    print(nombre.title()+" contiene la vocal a")
elif "e" in nombre:
    print(nombre.title()+" contiene la vocal e")
elif "i" in nombre:
    print(nombre.title()+" contiene la vocal i")
elif "o" in nombre:
    print(nombre.title()+" contiene la vocal o")
elif "u" in nombre:
    print(nombre.title()+" contiene la vocal u")
else:
    print("!que nombre tan extraño!!")
    
    
#*************************Ejemplos
# Operadores con varias listas:
    
lista1= [10,20,30]
lista2 =[40,50,60]

print(lista1 + lista2)

# mejorando la imprecion de varias listas

listaA = ["audi", "Toyota", "mazda"]
puerta =[2,4]

print ("Mi auto es: "+listaA[-1].title())
print (f"Mi auto {listaA[-2].title()} tiene {puerta[-2]} puertas")

# operadores matematicos de una lista:
    
lista3 =[100,500,200,7000,-200]

print(sum(lista3))       
print(max(lista3))       
print(min(lista3))

lista1 = list(range(7))                     
lista2 = list(range(1,10))                 
lista3 = list(range(-10,2))                     
lista4 = list(range(200,100,-20))               
lista5 = list(range(200,100,20))         

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

# ERROR COMUN EN UNA LISTA:
    
autos = ["mazda", "audi", "toyota","subaru","bwm","lamborghini"]


print(autos[6].upper())



autos = ["mazda", "audi", "toyota","subaru","bwm","lamborghini"]

print(autos[6].upper())


# Condicionales

### Hacer un programa que  determine si un numero ingresado por pantalla es positivo o negativo

x = int(input("Ingrese un nimero entero,positivo o negativo:"))
if x > 0:
    y ="positivo"
else:
    if x <0:
        y="negativo"
    else:
        if x == 0:
            y="cero"
print("\nEl numero :{}".format(x))
print("Es un numero : {}".format(y)) 


def det(xx) :
    if xx < 0:
        p="negativo"
    elif xx > 0:
        p ="positivo"
    else:
        p = "cero"
        print (p)
    return p

num = int(input("ingrese un numero entero, positivo o negativo :"))

resp =det(num)
print("\nEl Numero :  {}".format(num))
print("Es un numero :  {}".format(resp))

from math import pi

radio = float(input("ingrese el radio de un circulo: "))


#mmenu
print("selecione una opcion")
print("a) Calcular el diametro.")
print("b) Calcular el perimetro.")
print("c) Calcular el area.")
opcion =input("digita a, b, o c y preciona enter:    ")


if opcion =="a":
    diametro = 2 * radio
    print("\nEl diametro del circulo es {0}.".format(diametro))
else:
    if opcion=="b":
        perimetro = 2 * pi * radio
        print("\nEl perimetro del circulo es {0}.".format(perimetro))
    else:
        if opcion =="c":
            area = pi * radio **2
            print("\nEl perimetro del Circulo es {0}.".format(area))
        else:    
            print("\nSolo hay tres opciones: a, b, c.")
            print('Tu has teclado "{0}".'.format(opcion))
            
            
            
from math import pi

radio =float(input("ingrese el radio de un circulo"))


#Menù
print("seleccione una opcion: ")
print("a) Calcular el diametro.")
print("b) Calcular el perimetro.")      
print("c) Calcular el area.")    
opcion = input("Digita a, b, o c y presiona enter:   ")
if opcion== "a":
    diametro = 2* radio
    print("El perimetro del circulo es {0}.".format(diametro))
elif opcion == "b" :
        perimetro = 2 *pi *radio
        print("El perimetro del circulo es {0}.".format(perimetro))
elif opcion =="c":
    area = pi * radio **2
    print("el area del circulo es {0}.".format(area))
else:
    print("Solo hay tres opciones: a, b, c.")
    print('Tu has tecleado "{0}".'.format(opcion))


# Hacer un programa que varifique si se  ha comprado carne en la lista del mercado para hacer parrillad


alimento = ["arroz","papas","camotes","leche","carne","cebolla","tomate","lechuga"]

if "carne" in alimento:             
    print("Hoy  comemos rica Parrilla!!!!")
else:
    print("Hoy comeos verduras")
    


# Hacer un programa que verifique en una jugerua si tienen la fruta que deseas y prepare un jugo

def preparar (fruit):
    if fruit in fruta:
        print(f"\nSi tenemos {antojo.upper()} !!!, te prepararemos un jugo")
    else:
        print(f"\nHoy no tenemos {antojo.upper()},pero regresa mañana")
        
        
        

fruta=["platano","manzana","pera","naranja","mandarina","uva"]
antojo= input("ingresa la fruta que deseas comer hoy : ")

preparar(antojo)               


print("\nGracias por tu Preferencia !!!, Vuelve Pronto")


# Hacer un programa que verifique mayoria de edad

def mayoria(nom,xx):
    if xx>= 18:
        print(f'\n{nom.upper()} es Mayor de Edad con {xx} años de edad')
    else:
        print(f"\n{nom.upper()} es Menor de Edad con {xx} años de edad")    


nombre = input("ingresa tu nombre: ")
edad= int(input("ingrese su edad : "))
              
mayoria(nombre, edad)