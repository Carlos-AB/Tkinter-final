import librerias
import matriz
from tkinter import *
import numpy as np

pacientes = []
cama = []
numpaciente = 0
numcamas=0
dias=0
P=[]
i=1
while i==1:    
    #principal#
    print("==================================================")
    print("Desea ingresar a la interfaz?\n\t (1).Si. \n\t (2).No. ")
    print("==================================================")
    x = int(input("Elija opcion: "))
    #opcion 1:
    if x == 1:
        print ("Estadísticas Covid-19")
        j=1
        while j==1:
            numcamas =int(input("Ingrese el numero de camas UCI actual: "))
            if numcamas>-1:
                dispcamas=numcamas
                j=0
            else:
                mensaje_error()
                j=1
        
        z=1
        while z == 1:
            print ("Opciones: \n\t (1).Ingreso de datos.\n\t (2).Proyeccion.\n\t (3).Estadistica Actual.\n\t (4).Cerrar programa.")
            y =int(input("\tElija una opción (1-2-3-4): "))
            #opcion 1:
            if y == 1:
                print("----------------------------------------------------------")
                print(f"\tPacientes ingresados: {numpaciente}")
                print(f"\tCamas UCI actuales: {numcamas}")
                dias = dias + 1
                print("\tDías = "+str(dias)) 
                j=1
                while j==1:
                    valor1 = int(input("\tIndique la cantidad de pacientes nuevos: "))
                    if valor1>-1:
                        pacientes.append(int(valor1))
                        j=0
                    else:
                        mensaje_error()
                        j=1
                j=1
                while j==1:
                    valor2 = int(input("\tIndique la cantidad de camas UCI nuevas: "))
                    if valor2>-1:
                        cama.append(int(valor2))
                        j=0
                    else:
                        mensaje_error()
                        j=1
                
                numpaciente = numpaciente + valor1
                numcamas = numcamas + valor2
                print(f"\tLista de pacientes ingresados hasta Día {dias}: ")
                dispcamas=numcamas-numpaciente
                print("\tPacientes por día: ",pacientes)
                print("\tCamas agregadas por día",cama)
                if numcamas<numpaciente:
                    print("\tSITUACION CRÍTICA Falta de camas, se recomienda tomar medidas lo antes posible")
                else:
                    print("\tLa situacion Actual es estable")
                print("----------------------------------------------------------")
                
                z==1
            #opcion 2:    
            elif y == 2:
                print("----------------------------------------------------------")
                if dias>6:
                    B = split(pacientes, 7).copy()
                    a=0
                    for i in range(len(B)):
                        S=np.sum(B[i])
                        P.append(S)
                        a=a+1
                        if a == len(B):
                            PS = np.sum(P[a-2])
                            PP = int(PS/7)
                    print("\tRespecto a la semana anterior")
                    print("\tEl promedio de personas infectadas: ", PS)
                    print("\tEl promedio de personas infectadas por dia:", PP)

                    j=1
                    while j==1:
                        PY = int(input("\tIndique la que semana desea proyectar: "))
                        if PY>-1:
                            Proyeccion=PS*(1+(PP/100))**PY
                            print("\tSe estiman aproximadamente",Proyeccion,"infectados")
                            j=0
                        else:
                            mensaje_error()
                            j=1

                else:
                    print("\tEsta opcion unicamente esta habilitada a partir del dia 7")
                z==1
            #opcion 3:    
            elif y == 3:
                print("------------------------------------------------------------")
                print("\tEstadistica Actual")
                print("\t\tDia Actual",dias)
                print("\t\tCantidad de Infectados: ",numpaciente)
                print("\t\tCantidad de camas Totales",numcamas)
                if numcamas<numpaciente:
                    dispcamas = -dispcamas
                    print("\t\tCantidad de camas UCI faltantes", dispcamas)
                    dispcamas = -dispcamas
                else:
                    print("\t\tCantidad de camas Disponibles: ", dispcamas)
                print("\tEstado General:")
                if numcamas<numpaciente:
                    print("\t\tALERTA: FALTA DE CAMAS")
                else:
                    print("\t\tSITUACION ESTABLE")
            #opcion 4:    
            elif y== 4:
                print("-----------------------------------------------------")
                print("Programa cerrado")
                z = 0
            else:
                mensaje_error()
                z = 1
        i=0
    #opcion 2
    elif x== 2:
        print("----------------------------------------------------------")
        print("Progama cerrado")
        i=0
    elif x == 69:
        imagen()
    else:
        mensaje_error()
        i=1