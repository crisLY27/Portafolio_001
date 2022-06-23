"""
UNIVERSIDAD NACIONAL DE SAN AGUSTIN
ESCUELA PROFECIONAL DE INGENIERÌA EN TELECOMUNICACIONES
ALUMNO: LARICO YUCRA, CRISTHIAN DENIS
PRACTICA 6
"""

#  EXCEPCIONES Y FUNCIONES

# validacion de numeros:
while True:
    try:
        x = int(input("ingresar un numero: "))
        break
    except ValueError:
        
        print("error..!! no es un numero valido")
    
while True:
    try:
        x = int(input("ingresar un numero positivo : "))
        
    except ValueError:
        
        print("error..!! no es un numero positivo valido")
        continue
    if x < 0:
        print("\t porfavor ingrese numero positivo")
        continue
    break

# FUNCION PRINCIPAL main

def uno():
    print("inicio de pantalla")
def dos():
    pass
def fin():
    print("\n\n\n Fin del programa")
# programa MAIN PRINCIPIAL
if __name__=="__main__":
    uno()
    dos()
    uno()
    dos()

    fin()
    
# hacer un programa que verifique el ingreso del DNI correctamente



def validar_dni():
    while True:
        try:
            dni = int (input("ingresar DNI:"))
            if len(str(dni))==8:
                print("\n\t DNI VALIDO")
                break
            else:
                print("\t Error longitud de DNI no Valido")
                continue
        except ValueError:
            print("\t Error !!! **** No es un DNI valido...*** intente de nuevo***")
    return dni   
            
if __name__=="__main__":
    titulo=(" BONO FAMILIAR UNIVERSAL  ")
    print (titulo.center(50,"*"))
    print("\n\n")
    val_dni=validar_dni()
    print("\n \n El DNI Ingresando es:==>",val_dni)




# EJEMPLOS
import os

def menu():
    """
    funcion que limpia la pantalla y muestra nuevamente el menu
    """
    os.system("clear")
    titulo=("menu general  ")
    print (titulo.center(50,"*"))
    print("\n\n")
    print("selecciona una opccion ")
    print("\t1 - primera opcion")
    print("\t2 - segunda opcion")
    print("\t3 - tercera opcion")
    print("\t9- salir")
def validar():
    while True:
        menu()
        opcionMenu = input("inserta numero valor ==>>")
        
        if opcionMenu=="1":
            print("")
            input("has pulsado la opcion 1...\npulsa una tecla para continuar")
        elif opcionMenu=="2":
            print("")
            input("has pulsado la opcion 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
            print("")
            input("has pulsado la opcion 3...\npulsa una tecla para continuar")
        elif opcionMenu=="9":
            break
        else:
            print("")
            input("no has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")

    return opcionMenu

if __name__ == "__main__":
    validar()
    
    print("\t*****FINALIZO EL PROGRAMA****")



#fin del trabajo*********************
# EL PROFESOR DE COMPUTO ES EL MEJOR PROFESOR DEL MUNDO



























