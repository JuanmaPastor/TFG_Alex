# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 04:41:35 2020

@author: alech
"""

import os
import shutil

import pandas as pd

Opcion = input("""En el siguiente menú se describen las opciones 
               que puede realizar el usuario.
               El archico se guardará en la carpeta Sin_0
               Si se introduce más de un archivo, estos se concatenarán
               Aunque no se use el límite para quitar 0, se usa para escribir
               1 : Sólo quitar 0
               2 : Sólo trasponer
               3 : Sólo trasponer y añadir Clinical
               4 : Quitar 0 y trasponer
               5 : Quitar 0, trasponer y añadir Clinical
               6 : Salir
               
               Introduzca un número: """)

Opcion=int(Opcion)



def read():                                                                    #Lectura del excel con los datos de "Clinical" y convertir índices
    dl = pd.read_excel("metadata-cancer-pulmon2.xlsx")
    dl=dl.set_index("sample")
    return dl


def parts():                                                                   #Establecer el númeor de archivos que se quieren juntar
    Number = input("""Decida cuantos archivos quiere unir
               
               Introduzca un número: """)
    
    Number=int(Number)
    if type(Number) != int:
        print("Introduzca un número entero")
        parts()
    else:
        pass
    return Number

def read_parts():                                                              #Lectura de los Excels tras ser divididos anteriormente
    Number = parts()
    Pre_frames = [0]*Number
    if Number==1:
        Frag=input("""Introduzca el archivo que vaya a leer
                   : """)
        df = pd.read_excel()
        df=df.set_index("TAXA")
        
    else:
        for i in(0, Number-1):
            Frag=input("""Introduzca los archivos que vaya a unir de uno en uno
                  Introduzca el nombre del archivo: """)
            dp = pd.read_excel(Frag)      
            dp = dp.set_index("TAXA")
            Pre_frames[i] = dp
        
        df = pd.concat(Pre_frames, axis=1, sort=False)
    return df


def move(limite):
    carp = "Sin_0"
    try:
        os.makedirs(carp)
    except:
        print("\n Los archivos generados se moverán a la carpeta ya creada")
    
    try:
        shutil.move(limite + "Parse0.xlsx" , carp)
    except:
        print("No se ha podido mover el archivo")


def drpo(limite):
    df=read_parts()
    indices=df.index
    columnas=df.columns
    limit=int(limite)
    for j in (indices):
        Counter=0
        for i in (columnas):

            if df.loc[j, i] == 0:
                Counter=Counter+1
            else:
                pass            
            if limit==Counter:
                df=df.drop(index=j)
                break
            else:
                pass

    return df

def Transponse(limite, Opcion):                                                                  #Traspone las tablas divididas y
    if Opcion ==4:
        df = drpo(limite)
    else:       
        df = read_parts()            
    df = df.T

    df.to_excel(limite + "Parse0.xlsx") 
       
    return df

def Transponse_Clinical(limite, Opcion):
    dl = read()
    if Opcion ==5:
        df = drpo(limite)
    else:       
        df = read_parts() 
    df = df.T            
    
    indices=df.index    
    ref = dl.loc[indices, ["Clinical"]]
    df["Clinical"] = ref
    
    df.to_excel(limite + "Parse0.xlsx") 
    return df
    


def main():
    limite = input("""
                Introduzca el número a partir del cual se dropea la fila por la cantidad de 0 determinada: """) 

    if Opcion ==1:
        df=drpo(limite)
        df.to_excel(limite + "Parse0.xlsx") 
   
    elif Opcion==2 or Opcion==4:
        Transponse(limite, Opcion)
        
    elif Opcion==3 or Opcion == 5:
        Transponse_Clinical(limite, Opcion)
        
    elif Opcion==6:
        pass
    else:
        print("Introduzca un número válido la próxima vez")
        return
    move(limite)
    return

main()