# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 17:01:56 2020

@author: alech
"""

import os
import shutil

import pandas as pd

def read():
    df = pd.read_excel("metadata-cancer-pulmon2.xlsx")
    df=df.set_index("sample")
    return df

def parts():
    Number = input("""Decida cuantos archivos quiere unir
               
               Introduzca un número: """)
    
    Number=int(Number)
    if type(Number) != int:
        print("Introduzca un número entero")
        parts()
    else:
        return Number
               

def read_parts():
    Number = parts()
    Pre_frames = [0]*Number
    for i in(0, Number-1):
        Frag=input("""Introduzca los archivos que vaya a unir de uno en uno
              Introduzca el nombre del archivo: """)
        dp = pd.read_excel(Frag)      
        Pre_frames[i] = dp
    return Pre_frames


def Joiner():
    df = read()
    Pre_frames = read_parts()
    frames = [0] * len(Pre_frames)
    
    for i in (0,len(Pre_frames)-1):           #Hata aquí va bien
        dl = Pre_frames[i].T
        dl.columns=dl.iloc[0]
        ozo=dl.drop(index="TAXA")
        gf=ozo.index
    
        topo=df.loc[gf, ["Clinical"]]
        ozo["Clinical"] = topo
        frames[i]=ozo
        
    return frames

def Glue():
    frames = Joiner()
    joined = pd.concat(frames)
    joined.to_excel("Joined.xlsx")

Glue() 