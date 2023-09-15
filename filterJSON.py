import json
import csv
import pandas as pd

ruta_archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(ruta_archivo, "r") as archivo:
    data = archivo.read()

data = json.loads(data)

<<<<<<< HEAD
archivo = './data.csv'


for i in data["qubits"]:
    if(i[0]['name'] == 'T1'):
        datos_t1 = i[0]['value']
        data = {
            'T1': [datos_t1]
        }
        df = pd.DataFrame(data)
        print(df)
        df.to_csv(archivo, index=False)

        



    





for i in data["qubits"]:
    datos_t2 = i[1]

for i in data["gates"]:
    if(i['gate'] == 'rz'):
         datos_rz = i

for i in data["gates"]:
    if(i['gate'] == 'x'):
        datos_x = i
            
for i in data["gates"]:
    if(i['gate'] == 'sx'):
        datos_sx = i

for i in data["gates"]:
    if(i['gate'] == 'cx'):
        datos_cnot = i
=======
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
>>>>>>> 6c3146294f99d9985d13a51dc945cddfcaf4e2a8



