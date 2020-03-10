# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:23:47 2020

@author: alech
"""
import os
import shutil

import pandas as pd



lecture = input("""
                Introduzca el archivo que quira leer: """) 


def read(lecture):                                                              #Lectura del excel con los datos de "Clinical" y convertir índices                                                                 
    df = pd.read_excel(lecture)
    df=df.set_index("TAXA")
    return df

def move(lecture):
    carp = "Frequencies"
    try:
        os.makedirs(carp)
    except:
        print("\n Los archivos generados se moverán a la carpeta ya creada")
    
    try:
        shutil.move("Freq_" + lecture, carp)
    except:
        print("No se ha podido mover el archivo")
    

def freq():
    df = read(lecture)
    fr = df/df.sum()
    fr.to_excel("Freq_" + lecture)
    
def main(): 
    freq()
    move(lecture)

main()