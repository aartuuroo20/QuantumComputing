import json
import csv
import pandas as pd

ruta_archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(ruta_archivo, "r") as archivo:
    data = archivo.read()

data = json.loads(data)

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



