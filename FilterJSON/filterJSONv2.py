import json
import pandas as pd

ruta_archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(ruta_archivo, "r") as archivo:
    data = archivo.read()

data = json.loads(data)

datos_t1 = []
datos_t2 = []

nombre = data['qubits'][0][0]['name']
print(nombre)

'''
for i in data['qubits']:
    for a in range(len(i)):
        if i[a]['name'] == 'T1':
            datos_t1.append(i[a]['value'])
        elif i[a]['name'] == 'T2':
            datos_t2.append(i[a]['value'])
'''

t1 = list(filter(lambda x: x['name'] == 'T1', data['qubits']))
print(t1)

