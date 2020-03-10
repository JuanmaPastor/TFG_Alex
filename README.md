# TFG_Alex

El programa usa datos de pacientes de cáncer de pulmón.

Por el momento cuenta con un Reader_Steiner.py para separar los pacientes sanos de los enfermos y posteriormente se separan por la localización de la muestra en el excel de metadata. Posteriormente coge los pacientes tras el filtrado y con el excel de la tabla-cancer coge los datos de bacterias de los pacientes filtrados. Por último guarda los resultado0s en varias carpetas.

También tiene un Joiner_Steiner.py que permite quitar bacterias con la cantidad de valores nulos que especifique el usuario, unir tablas y añadir a las bacterias la columna de Clinical para un posterior análisis.

El Frequence_Steiner.py convierte los valores de las columnas en frecuencias.
