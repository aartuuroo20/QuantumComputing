import json
import csv
import pandas as pd

ruta_archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(ruta_archivo, "r") as archivo:
    data = archivo.read()

data = json.loads(data)

archivo_t1 = "archivo_t1.txt"

datos_t1 = {}


for i in data["qubits"]:   
    if(i[0]['name'] == 'T1'):
        datos_t1 = i[0]
        with open(archivo_t1, "w") as archivo:
            archivo.write(str(datos_t1))
        
def filterJSONT2(data):
    for i in data["qubits"]:
       datos_t2 = i[1]

def filterJSONRz(data):
    for i in data["gates"]:
        if(i['gate'] == 'rz'):
            datos_rz = i
        elif (i['gate'] == 'x'):
            datos_x = i
        elif(i['gate'] == 'sx'):
            datos_sx = i
        elif(i['gate'] == 'cx'):
            datos_cnot = i


filterJSONT2(data)
filterJSONRz(data)



