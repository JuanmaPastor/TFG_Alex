# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:09:47 2020

@author: alech
"""

import os
import shutil

import pandas as pd

#---------------------------------------------------------------------------
#-----------SECCION DE LECTURA DE ARCHIVOS---------------------------------

def read():                                                                    #Lectura del Excel con los metadatos
    df = pd.read_excel("metadata-cancer-pulmon2.xlsx")    
    return df

def read_heal():                                                               #Lectura del Excel con los pacientes sanos
    if os.path.isfile("heal.xlsx")==True:
        dh = pd.read_excel("heal.xlsx")
    else:
        print("No hay un archivo con los sanos")
    return dh

def read_sick():                                                               #Lectura del Excel con los pacientes enfermos
    if os.path.isfile("sick.xlsx")==True:
        ds = pd.read_excel("sick.xlsx")
    else:
        print("No hay un archivo con los enfermos")
    return ds

#------------------------------------------------------------------
#----------SECCION DE MOVIMIENTO DE FICHEROS DE RESULTADOS---------

def move_heal():                                                               #Mueve los resultados de pacientes sanos
    Results = "Heal_Results"
    try:
        os.makedirs(Results)
    except:
        print("Ya hay una carpeta de resultados creada para los pacientes sanos")
        
    try:
        shutil.move("heal.xlsx", Results)
        shutil.move("healthy_lung.xlsx", Results)
        shutil.move("healthy_saliva.xlsx", Results)
    except:
        print("No se ha podido mover los excel generados a la carpeta de resultados")

def move_sick():                                                               #Mueve los resultados de pacientes enfermos
    Results = "Sick_Results"
    try:
        os.makedirs(Results)
    except:
        print("Ya hay una carpeta de resultados creada para los pacientes enfermos")
        
    try:
        shutil.move("sick.xlsx", Results)
        shutil.move("affected_lung.xlsx", Results)
        shutil.move("sick_saliva.xlsx", Results)
        shutil.move("faeces.xlsx", Results)
        shutil.move("contralateral_lung.xlsx", Results)
    except:
        print("No se ha podido mover los excel generados a la carpeta de resultados")
        
#-----------------------------------------------------------------------
#---------------SECCIÓN DE FUNCIONES DE SEPARACIÓN DE DATOS ------------                   
                    
def separate_clinical():                                                       #Separa enfermos y sanos y genera 2 Excels con los resulados
    if os.path.isfile("heal.xlsx")==True  or os.path.exists("sick.xlsx")==True:
        print("Ya hay un archivo con los sanos o con los enfermos separados")

    else:
        led=read()                                                             #Ejecuta la lectura del Excel
        lect = led.set_index("Sample-ID")                                      #Cambia los índices por el identificador del paciente
        heal=(lect["Clinical"] == "healthy")                                   #Selecciona los sanos
        lect.loc[heal, [ "Clinical", "Location"]].to_excel("heal.xlsx")        #Escribe en un Excel las columnas seleccionadas de los sanos
    
        sick=(lect["Clinical"] == "sick")
        lect.loc[sick, ["Clinical", "Location"]].to_excel("sick.xlsx")
    
    return

def sep_heal_location():                                                       #Dentro de los sanos separa por lugar de toma de muestra
    if os.path.isfile("healthy_lung.xlsx")==True:
        print("Ya hay un archivo con los healthy_lung de pacientes sanos")
    else:
        led = read_heal()
        lect = led.set_index("Sample-ID")
        lung=(lect["Location"]== "healthy-lung")
        lect.loc[lung, ["Clinical", "Location"]].to_excel("healthy_lung.xlsx")
    
    if os.path.isfile("healthy_saliva.xlsx")==True:
        print("Ya hay un archivo con los healthy_lung de pacientes sanos") 
    else:
        led = read_heal()
        lect = led.set_index("Sample-ID")
        saliva=(lect["Location"]) == "saliva-from-controls"
        lect.loc[saliva, [ "Clinical", "Location"]].to_excel("healthy_saliva.xlsx")
    
    return
    
def sep_sick_location():                                                       #Dentro de los enfermos separa por lugar de toma de muestra
    if os.path.isfile("affected_lung.xlsx")==True:
        print("Ya hay un archivo con los affected_lung de pacientes enfermos")
    else:
        led = read_sick()
        lect = led.set_index("Sample-ID")
        lung=(lect["Location"]== "affected-lung")
        lect.loc[lung, ["Clinical", "Location"]].to_excel("affected_lung.xlsx") 
        
    if os.path.isfile("sick_saliva.xlsx")==True:
        print("Ya hay un archivo con los sick_saliva de pacientes enfermos") 
    else:
        led = read_sick()
        lect = led.set_index("Sample-ID")
        lung=(lect["Location"]== "saliva-from-patients")
        lect.loc[lung, ["Clinical", "Location"]].to_excel("sick_saliva.xlsx")

    if os.path.isfile("faeces.xlsx")==True:
        print("Ya hay un archivo con los faeces de pacientes enfermos") 
    else:
        led = read_sick()
        lect = led.set_index("Sample-ID")
        lung=(lect["Location"]== "faeces")
        lect.loc[lung, ["Clinical", "Location"]].to_excel("faeces.xlsx") 

    if os.path.isfile("contralateral_lung.xlsx")==True:
        print("Ya hay un archivo con los contralateral_lung de pacientes enfermos") 
    else:
        led = read_sick()
        lect = led.set_index("Sample-ID")
        lung=(lect["Location"]== "contralateral-lung")
        lect.loc[lung, ["Clinical", "Location"]].to_excel("contralateral_lung.xlsx") 
        
    return

#---------------------------------------------------------------------------------------------
#--------SECCION DE EJECUCION DE LAS FUNCIONES CREADAS -------------------------------------
    
Opcion = input("""El programa puede realizar las siguientes funciones:         
               1. Dividir por pacientes enfermos/sanos y localización 
                  de la muestra               
               2. Dividir solo entre enfermos y sanos
               3. Dividir solo entre la localizacion de la muestra tras tener 
                  la division previa
               4. Todo lo anterior Y además guardar los resultados en carpetas 
                  de resultados
               5. Salir
               Introduzca un número: """)


def main(Opcion):                                                              #Ejecuta las funciones según la opción escogida

    if Opcion == "1":
        separate_clinical()
        
        sep_heal_location()
        
        sep_sick_location()
        
    elif Opcion =="2":
        separate_clinical()
    
    elif Opcion =="3":  
        sep_heal_location()
        
        sep_sick_location()
    
    elif Opcion =="4":
        separate_clinical()
        
        sep_heal_location()
        move_heal()
        
        sep_sick_location()
        move_sick()
    
    elif Opcion =="5":
        print("\nHa salido del programa ")
    
    else:
        print("\nHa introducido un número no válido, va a salir del programa")
    
    return
    
main(Opcion)    
    
    
   
