# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 00:42:37 2020

@author: alech
"""

import pandas as pd
import tkinter as tk


class Joiner:
    def __init__(self, master):
        self.master = master
        master.title("Multi Joiner")

        self.label1 = tk.Label(master, text="Si se ponen 2 archivos se concatenan")
        self.label1.grid(row=0)
        
        self.label2 = tk.Label(master, text="Primer archivo : ")
        self.label2.grid(row=1, column=0)
        self.entry1 = tk.Entry(master)
        self.entry1.grid(row=1, column=1, padx=50)
        
        self.label3 = tk.Label(master, text="Segundo archivo (opcional) : ")
        self.label3.grid(row=2, column=0)        
        self.entry2 = tk.Entry(master)
        self.entry2.grid(row=2, column=1, padx=50)
        
        
        self.label4 = tk.Label(master, text="Tercer archivo (opcional) : ")
        self.label4.grid(row=3, column=0)
        self.entry3 = tk.Entry(master)
        self.entry3.grid(row=3, column=1, padx=50)
        
        
        self.label5 = tk.Label(master, text="Limite de pacientes sin bacteria (numero): ")
        self.label5.grid(row=4, column=0)
        self.limit = tk.Entry(master)
        self.limit.grid(row=4, column=1)
        
        self.Op = tk.LabelFrame(master, text="Opciones del programa")
        self.Op.grid(row=5, column=0)
        
        self.opcion = tk.IntVar()
        
        self.Op1 = tk.Radiobutton( self.Op, text="Solo quitar por limite", variable=self.opcion, value=1).pack()
        self.Op2 = tk.Radiobutton( self.Op, text="Solo trasponer", variable=self.opcion, value=2).pack()
        self.Op3 = tk.Radiobutton( self.Op, text="Solo trasponer y añadir Clinical", variable=self.opcion , value=3).pack()
        self.Op4 = tk.Radiobutton( self.Op, text="Quitar 0 y trasponer", variable=self.opcion , value=4).pack()
        self.Op5 = tk.Radiobutton( self.Op, text="Quitar Ceros, trasponer y añadir Clinical", variable=self.opcion , value=5).pack()
        
        
        self.launch_button = tk.Button(master, text="Launch", command=self.launch)
        self.launch_button.grid(row=6, column=1)
        
        self.helpo_button = tk.Button(master, text="Help", command=self.helpo)
        self.helpo_button.grid(row=6, column=0)
        
        
    
    def helpo(self):
        tk.messagebox.showinfo("AYUDA","""
        Si se introducen 2 archivos se concatenan
        Para unir 4 o más archivos usar la primera opción 
        varias veces con un limite muy alto
        
        El limite es el número de pacientes que tienen 0 
        de una determinada bacteria, a partir del cual 
        se elimina esa bacteria del archivo 
        (cuanto más bajo sea más presente estará la bacteria)
        Las Opciones de quitar 0 hacen referencia al uso
        del límite
        
        Los archivos de entrada pueden proceder del 
        Reader.Steiner o el Frequence.Stiener
        Si no se encuentran los archivos, poner la ruta absoluta
        
        Para añadir Clinical se reuiere que el programa
        se encuentre en el mismo directorio donde este el 
        archivo: metadata-cancer-pulmon2.xlsx
        
        Añadir Clinical indica que añade una última columna
        que indica la condición clínica del paciente 
        de la muestra""")
    
    
    def read(self):                                       #####Leemos el original para asignar la condición clínica                                                         
        self.dl = pd.read_excel("metadata-cancer-pulmon2.xlsx")
        self.dl = self.dl.set_index("sample")  #########
        


    def parts(self):                                     ###Comprobamos el número de archivos como inputs                                                            
        self.Entrada1 = self.entry1.get()
        self.Entrada2 = self.entry2.get()
        self.Entrada3 = self.entry3.get()
        
        if len(self.Entrada3) > 1:
            self.Number = 3
        elif len (self.Entrada2) > 1:
            self.Number = 2
        elif len(self.Entrada1) > 1:
            self.Number = 1
        else:
            tk.messagebox.showinfo("Error","Introduzca el nombre de un archivo")
            
            
    def read_parts(self): 
                                                                          
        if self.Number==1:
            try:
                self.df = pd.read_excel(self.Entrada1)
                self.df = self.df.set_index("TAXA")
            except:
               tk.messagebox.showinfo("Error","Problema al leer el archivo") 
            
        elif self.Number==2:
            try:
                self.dk1 = pd.read_excel(self.Entrada1)      
                self.dk1 = self.dk1.set_index("TAXA")
                
                self.dk2 = pd.read_excel(self.Entrada2)      
                self.dk2 = self.dk2.set_index("TAXA")
                
                Pre_frames = [self.dk1, self.dk2]
                
                self.df = pd.concat(Pre_frames, axis=1, sort=False)
            except:
               tk.messagebox.showinfo("Error","Problema al leer el archivo")        

        elif self.Number==3:
            try:
                self.dj1 = pd.read_excel(self.Entrada1)      
                self.dj1 = self.dj1.set_index("TAXA")
                
                self.dj2 = pd.read_excel(self.Entrada2)      
                self.dj2 = self.dj2.set_index("TAXA")
                
                self.dj3 = pd.read_excel(self.Entrada3)      
                self.dj3 = self.dj3.set_index("TAXA")
                
                Pre_frames = [self.dj1, self.dj2, self.dj3]
                
                self.df = pd.concat(Pre_frames, axis=1, sort=False)
            except:
               tk.messagebox.showinfo("Error","Problema al leer el archivo") 

        self.columnas = self.df.columns
        tk.messagebox.showinfo("Total de columnas","\nHay un total de {} pacientes en el Dataframe".format(len(self.columnas)))    
    
    #----------------------------------------------------------------------------
    #----------------ELIMINAR BACTERIAS CON X CEROS------------------------------
    #----------------------------------------------------------------------------
    
    def drpo(self):                      #Quita las bacterias menos presentes
        self.indices = self.df.index
        self.columnas = self.df.columns
        self.limite = self.limit.get()
        
        for j in (self.indices):
            self.Counter = 0
            for i in (self.columnas):   
                if self.df.loc[j, i] == 0:
                    self.Counter = self.Counter+1
                else:
                    pass 
                if int(self.limite) == self.Counter:
                    self.df= self.df.drop(index=j)
                    break
                else:
                    pass

    #-----------------------------------------------------------------------------
    #-------------TRASPONER-------------------------------------------------------
    #-----------------------------------------------------------------------------
    
    def Transponse(self):     #Transpone                                                               
            
        self.dn = self.df.T
        self.dn.index.name ="Muestras"    
    
    #-----------------------------------------------------------------------------
    #-------------TRASPONER Y AÑADIR CLINICAL-------------------------------------
    #-----------------------------------------------------------------------------
    
    def Transponse_Clinical(self):     #Transpone y añade la categoría de Clinical
        self.dn = self.df.T          
        
        self.indic = self.dn.index    
        self.ref = self.dl.loc[self.indic, ["Clinical"]]
        self.dn["Clinical"] = self.ref    
        
        try: 
            self.contralateral = (self.dl["Location"] == "contralateral-lung")  #Se crea una categoría especial para los contralateral lung en Clinical
            self.contra = self.dl[self.contralateral]
            self.ind = self.contra.index
            self.dn.loc[self.ind, ["Clinical"]] = ["Special"]
        except:
            print("no hay contralateral")

        self.dn.index.name ="Muestras"
             
    
    def launch(self):                                     #Lanzador
        try:
            self.Option= self.opcion.get()
            
            self.parts()
            
            self.read_parts()
            
            if self.Option == 1:
                self.drpo()
                self.df.to_excel("Sin0.xlsx")
            
            elif self.Option == 2:
                self.Transponse()
                self.dn.to_excel("Traspuesto.xlsx")
            
            elif self.Option == 3:
                self.read()
                self.Transponse_Clinical()
                self.dn.to_excel("Traspuesto_Clinical.xlsx")
                
            elif self.Option == 4:
                self.drpo()
                self.Transponse()            
                self.dn.to_excel("Sin0_Traspuesto.xlsx")
                
            elif self.Option == 5:
                self.read()
                self.drpo()
                self.Transponse_Clinical()
                self.dn.to_excel("Sin0_Traspuesto_Clinical.xlsx")
            
            else:
                tk.messagebox.showinfo("Error","Escoja una opción")
                
            tk.messagebox.showinfo("Finalización","La ejecución ha finalizado con éxito")
            
        except:
            tk.messagebox.showerror("Error", "No se ha podido ejecutar el programa")


root= tk.Tk()
my_gui = Joiner(root)
root.mainloop()


