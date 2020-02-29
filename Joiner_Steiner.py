# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:01:56 2020

@author: alech
"""

import pandas as pd

#-----------------------------------------------------------------------------
#--------FUNCIONES DE LECTURA Y SOPORTE DE LOS DATAFRAMES---------------------
#-----------------------------------------------------------------------------

def read():                                                                    #Lectura del excel con los datos de "Clinical" y convertir índices
    df = pd.read_excel("metadata-cancer-pulmon2.xlsx")
    df=df.set_index("sample")
    return df

def parts():                                                                   #Establecer el númeor de archivos que se quieren juntar
    Number = input("""Decida cuantos archivos quiere unir
               
               Introduzca un número: """)
    
    Number=int(Number)
    if type(Number) != int:
        print("Introduzca un número entero")
        parts()
    else:
        return Number
               

def read_parts():                                                              #Lectura de los Excels tras ser divididos anteriormente
    Number = parts()
    Pre_frames = [0]*Number
    for i in(0, Number-1):
        Frag=input("""Introduzca los archivos que vaya a unir de uno en uno
              Introduzca el nombre del archivo: """)
        dp = pd.read_excel(Frag)      
        Pre_frames[i] = dp
    return Pre_frames

# -----------------------------------------------------------------------------
#-------------FUNCIONES PARA JUNTAR LAS TABLAS---------------------------------
#------------------------------------------------------------------------------

def Joiner():                                                                  #Traspone las tablas divididas y les añade la columna "Clinical"
    df = read()
    Pre_frames = read_parts()
    frames = [0] * len(Pre_frames)
    
    for i in (0,len(Pre_frames)-1):           
        dl = Pre_frames[i].T
        dl.columns=dl.iloc[0]
        post_dl=dl.drop(index="TAXA")
        indices=post_dl.index
    
        ref = df.loc[indices, ["Clinical"]]
        post_dl["Clinical"] = ref
        frames[i]=post_dl
        
    return frames

def Glue():                                                                    #Concatena los Dataframes
    frames = Joiner()
    joined = pd.concat(frames)
    joined.to_excel("Joined.xlsx")

def main():
    Glue() 

main()