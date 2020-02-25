# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:29:54 2020

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

def read_bact():                                                               #Lectura de la Tabla, los sample pasan a ser las columnas
    ds = pd.read_excel("tabla-cancer-pulmon2.xlsx")
    ds.columns=ds.iloc[0]
    ds.rename(columns={"#TAXA ID": "TAXA"}, inplace=True)
    ds.set_index("TAXA", inplace=True)
    bact=ds.drop(index="#TAXA ID")
    
    return bact

def read_heal():                                                               #Lectura del Excel con los pacientes sanos
    if os.path.isfile("Heal_Ref.xlsx")==True:
        dh = pd.read_excel("Heal_Ref.xlsx")
    else:
        print("No hay un archivo con los sanos")
    return dh

def read_sick():                                                               #Lectura del Excel con los pacientes enfermos
    if os.path.isfile("Sick_Ref.xlsx")==True:
        dt = pd.read_excel("Sick_Ref.xlsx")
    else:
        print("No hay un archivo con los enfermos")
    return dt

#------------------------------------------------------------------
#----------SECCION DE MOVIMIENTO DE FICHEROS DE RESULTADOS---------

def move_reference():
    Results = "Clinical_References"
    try:
        os.makedirs(Results)
    except:
        print("Ya hay una carpeta con las referencias creadas")
        
    try:
        shutil.move("Heal_Ref.xlsx", Results)
        shutil.move("Sick_Ref.xlsx", Results)
    except:
        print("No se ha podido mover los excel con referencias")
        

def move_heal():                                                              
    Results = "Heal_Results"
    try:
        os.makedirs(Results)
    except:
        print("Ya hay una carpeta de resultados creada para los pacientes sanos")
        
    try:
        shutil.move("Heal_Bact.xlsx", Results)
        shutil.move("Heal_Lung_Bact.xlsx", Results)
        shutil.move("Heal_Saliva_Bact.xlsx", Results)
    except:
        print("No se ha podido mover los excel generados a la carpeta de resultados")

def move_sick():                                                               
    Results = "Sick_Results"
    try:
        os.makedirs(Results)
    except:
        print("Ya hay una carpeta de resultados creada para los pacientes enfermos")
        
    try:
        shutil.move("Sick_Bact.xlsx", Results)
        shutil.move("Sick_Affected-lung_Bact.xlsx", Results)
        shutil.move("Sick_Saliva_Bact.xlsx", Results)
        shutil.move("Sick_Faeces_Bact.xlsx", Results)
        shutil.move("Sick_Contralateral-lung_Bact.xlsx", Results)
    except:
        print("No se ha podido mover los excel generados a la carpeta de resultados") 

    
#-----------------------------------------------------------------------
#---------------SECCIÓN DE FUNCIONES DE SEPARACIÓN DE DATOS ------------                   
                    
def separate_clinical():                                                       #Separa enfermos y sanos y genera 2 Excels con los resulados
    if os.path.isfile("heal.xlsx")==True  or os.path.exists("sick.xlsx")==True:
        print("Ya hay un archivo con los sanos o con los enfermos separados")

    else:
        led=read() 
        ds = read_bact()
        lect = led.set_index("Sample-ID")                                      #Cambia los índices por el identificador del paciente
        
        filt_heal = (lect["Clinical"] == "healthy")
        lect.loc[filt_heal, ["Clinical", "Location"]].to_excel("Heal_Ref.xlsx")
        dividir_heal = lect[filt_heal]
        indices_heal = dividir_heal.index
        ds[indices_heal].to_excel("Heal_Bact.xlsx")
        
        filt_sick = (lect["Clinical"] == "sick")
        lect.loc[filt_sick, ["Clinical", "Location"]].to_excel("Sick_Ref.xlsx")
        dividir_sick = lect[filt_sick]
        indices_sick = dividir_sick.index
        ds[indices_sick].to_excel("Sick_Bact.xlsx")        
        
        return 

def separate_heal():
    led = read_heal()
    ds = read_bact()
    lect = led.set_index("Sample-ID")
    
    
    filt_saliva = (lect["Location"] == "saliva-from-controls")
    dividir_saliva = lect[filt_saliva]
    indices_saliva = dividir_saliva.index
    ds[indices_saliva].to_excel("Heal_Saliva_Bact.xlsx")

    filt_lung = (lect["Location"] == "healthy_lung")
    dividir_lung = lect[filt_lung]
    indices_lung = dividir_lung.index
    ds[indices_lung].to_excel("Heal_Lung_Bact.xlsx")


def separate_sick():
    led = read_sick()
    ds = read_bact()
    lect = led.set_index("Sample-ID")    

    filt_saliva = (lect["Location"] == "saliva-from-patients")
    dividir_saliva = lect[filt_saliva]
    indices_saliva = dividir_saliva.index
    ds[indices_saliva].to_excel("Sick_Saliva_Bact.xlsx")

    filt_contralateral = (lect["Location"] == "contralateral-lung")
    dividir_contralateral = lect[filt_contralateral]
    indices_contralateral = dividir_contralateral.index
    ds[indices_contralateral].to_excel("Sick_Contralateral-lung_Bact.xlsx")
    
    filt_lung = (lect["Location"] == "affected-lung")
    dividir_lung = lect[filt_lung]
    indices_lung = dividir_lung.index
    ds[indices_lung].to_excel("Sick_Affected-lung_Bact.xlsx")
    
    filt_faeces = (lect["Location"] == "faeces")
    dividir_faeces = lect[filt_faeces]
    indices_faeces = dividir_faeces.index
    ds[indices_faeces].to_excel("Sick_Faeces_Bact.xlsx")


#---------------------------------------------------------------------------------------------
#--------SECCION DE EJECUCION DE LAS FUNCIONES CREADAS -------------------------------------
    
Opcion = input("""El programa puede realizar las siguientes funciones:         
               1. Dividir por pacientes enfermos/sanos y localización 
                  de la muestra               
               2. Ejecutar la anterior opción y guardar los resultados
               3. Salir del programa
               
               Introduzca un número: """)


def main(Opcion):                                                              #Ejecuta las funciones según la opción escogida

    if Opcion == "1":
        separate_clinical()
        
        separate_heal()
        
        separate_sick()
        
    elif Opcion =="2":
        separate_clinical()
        
        separate_heal()
        
        separate_sick()
        
        move_reference()
        
        move_heal()
        
        move_sick()
    
    elif Opcion =="3":
        print("\nHa salido del programa ")
    
    else:
        print("\nHa introducido un número no válido, va a salir del programa")
    
    return
    
main(Opcion)    
    
    
   
