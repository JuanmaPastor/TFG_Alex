# TFG_Alex

El programa usa datos de pacientes de cáncer de pulmón.

Por el momento cuenta con un Reader_Steiner.py para separar los pacientes sanos de los enfermos y posteriormente se separan por la localización de la muestra en el excel de metadata. Posteriormente coge los pacientes tras el filtrado y con el excel de la tabla-cancer coge los datos de bacterias de los pacientes filtrados. Por último guarda los resultados en varias carpetas. Tiene además una interfaz gráfica sencilla

También tiene un Joiner_Steiner.py que permite quitar bacterias con la cantidad de valores nulos que especifique el usuario, unir tablas y añadir a las bacterias la columna de Clinical para un posterior análisis.
El Multi_Joiner.py es la versión con interfaz gráfica del Joiner.py

El Frequence_Steiner.py convierte los valores de las columnas en frecuencias y cuenta con una interfaz gráfica.

La carpeta log_mean_var contiene un archivo .ipynb y varios excel donde se puede ver la relación que existe entre el log de la media de las bacterias con respecto al log de la varianza

La carpeta log_mean_var contiene un archivo .ipynb y varios excel donde se puede ver que la media relativa de las bacterias sigue una distribución Log_Normal

El archivo Orange_Cancer.ows se abre con Orange.biolab (se puede encontrar dentro de Anaconda) y permite realizar varios análisis de aprendizaje automático con los archivos generados por el Multi_Joiner.py

