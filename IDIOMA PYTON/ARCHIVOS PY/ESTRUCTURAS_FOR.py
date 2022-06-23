"""
****************************UNIVERSIDAD NACIONAL DE SAN AGUSTIN***************************




**********************ESCUELA PROFECIONAL DE INGENIERÌA EN TELECOMUNICACIONES**********************



ALUMNO: LARICO YUCRA, CRISTHIAN DENIS



***********************************PRACTICA 4*****************************
"""

# ESTRUCTURA ITERATIVAS

# ESTRUCTURA ITERATIVAS - bucle FOR

# FOR


num=[200,8,1500,10]
for o in num:
    print(o)
    
amor="el", "amor", "de", "mi", "vida", "cumple", "años", "hoy"
for r in amor:
    print(r)
    
yo="CRISTHIANLARICOYUCRA"
for r in yo:
    print(r)
    
    
for nombre in ["cristhiancito","cesitar","jhordancito","rudycito","manucito"]:
    print("hola {0} la longitud de tu nombre es de : {1} caracteres. " .format(nombre,len(nombre)))
    
# Hacer un programa que integre a lo largo de una lista que contenga colores y añada (appends) todos los colores que contengan la letra r a una  nueva lista 
          

colo=["pink","blue","green","purple","yellow","black"]

colo_con_r = []

for m in colo:
    if "r" in m:
        colo_con_r.append(m)
print(colo_con_r)

# <center> FUNCION RANGE( )
for i in range(22):
    print(i)
print("mi edad #estoy_viejo")

# hacer un programa que imprima del numero 1 al 10

for u in range(22):
    print(u +  1,"",end="")
    
for u in range(1,22):
    print(u,  "  ",end="")
    
    

for u in range(2,10,2):
    print(u,"  ",end=   "  ")

for u in range(20,0,-2):
    print(u,"",end="")




for u in range(20,0,-2):
    print(u,"",end="")




for u in range(40,-5,-5):
    print(u,"",end="")


for u in range(50,-1,-5):
    print(u,"",end="")
    
    
# MODIFICANDO LA INTEGRACION DE BUVLE FOR: BREAK Y CONTINUE
# Uso de break 
    
lista1=[2,4,5,7,8,9,3,4]
conta= 0

for m in lista1:
    conta = conta + 1
    if m == 9 :
        break
        
print(conta)

#Asignacion Abreviada 


contador = 1

contador /= 5                        
c=1 
c+=1
print(c)





lista1 = [2,4,5,7,8,19,3]


cont= -1

for m in lista1:
    cont +=  1
    if m == 9 :
        break

else:
    cont = -1
    print("no se encontro el numero 9 ")
    
if cont >= 0:
    print(cont)
    


#Uso de continue:
    

numero=[15,17,19,22,28,29,34,36,45,57,95,100]

for p in numero:
    if p % 2 !=0:
        continue
    print(p)
    
# fin de la practica numero 4 




#***************EJEMPLO******************


# ESTRUCTURA INTERACTIVA " For" 


# 1) HACER UN PROGRAMA MOSTRANDO POR LA PANTALLA LOS NUMEROS PARES DEL 0 AL 10:

for num in range(0,11,2):
    print(num)
    
    
    
# 2) Hacer unprograma que permita nombres a  una lista, utilizando funciones

nombres =[]

def ingreso(ele):
    for i in range(0,ele):
        m=input("ingresar nombre de la posicion {0}:".format(i))
        nombres.append(m)
T=int(input("de cuantos elementos crearemos la lista de nombres:"))

ingreso(T)

print("\n la lista completa de nombres es: \n",nombres)


# METODO 2 HACER UN PROGRAMA QUE DE UNA LISTA DE NUMEROS QUE IMPRIMA LA PISICION DEL NUMERO 9, UTILIZANDO FUNCION ENUMERATE

lista = [2,12,13,15,16,22,25,28]


for i,m in enumerate(lista):
    if m == 9:
        break
        
else:
    i= -1
    print("no se encontro el numero 9 eso quiere decir que no hay en tu lista no hay 9  pues, tu puedes no te desanimes xd")
    
if i >= 0:
    print(i)




# Hacer un programa que le a la lista de libro de Mario Vargas Llosa e indique el orden de los libros

libros_de_mvll=["La ciudad de los perros","La casa verde","Pantaleon y las visitadoras"]

orden=["primer","segundo","tercer"]

for i, libros in enumerate(libros_de_mvll):
    print("\n El " + orden[i] +" libro de Mario Llosa es:"+ libros)


# Hacer un programa que realice invitaciones de una lista de nombres .

for f in ["CESAR","JHORDAN","CRISTHIAN","RUDY","MANUEL","PROFESOR"]:
    invitacion= "Hola "+ f + " ¡estas invitado a una super fiesta el 30 de diciembre !"
    print(invitacion)
    print("traes comida :3 menos el PROFESOR c:")

# Hacer un programa que sume los elementos de una lista , USAR funciones y listas 


def mysum(xs):
    runnig_total=0
    for x in xs:
        runnig_total=runnig_total+x
    return runnig_total



print(mysum([1 ,2 ,3 , 4]))                    
print(mysum([1.25 ,2.5 ,1.75]))               
print(mysum([1, -2,  3]))                       
print(mysum([1, 2, 3,4  ]))                      
print(mysum(range(11)))                     
print(mysum([]))

# Hacer un programa que sume los elementos de una lista usando una funcion sum


m=[1 ,2 ,3 ,4]
sum(m)

# Hacer un programa que imprima los multiplos hasta el 10 de cualquier numero

def multiplos (n):
    for i in range(1, 11):
        print(n * i, end="  ")
    print()

m=int(input("Ingrese un numero: "))
print ("\n Los multiplos de ", m ," son: ")
multiplos(m)



#Ejemplo de FOR animado : creacion de tabla

for A in range(0,4):
    for C in range(0,4):
        for M in range(0,2):
            print(A,C,M)
            
            
# Hacer un programa que permita hallar la raiz enesima de un numero que se ingresara por teclado



numero = float(input("Ingrese un numero: "))

for n in range (2,101):
    print("la raiz {0} - enesima de {1} es {2} ".format(n,numero,numero**(1/n)))
    
    
num=["1","2","3","4","5","6","7","8","9","0"]
sim=["?","!","$","%","&","/","°","~"]

def validar(nomap):
    for x in nomap:
        if x in num:
            print("Nombre no valido!!!")
        elif x in sim:
            print("Nombre no valido!!!")
        else:
            print("Nombre valido")


            
            
nom=input("Ingrese su nombre: ")
 
validar(nom)


apell=input("Ingrese su apellido: ")




validar(apell)   

# FINALIZANDO LA PRACTICA NUMERO 4 


# PORFA AQUI TAMPOCO COPIEN MI REPOSITORIO, EL PROFE ME VA A JALAR Y NOS BOTARA DEL CURSO  YO YA TENGO MIEDO.



























