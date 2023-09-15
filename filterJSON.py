import json
import csv
import pandas as pd

ruta_archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(ruta_archivo, "r") as archivo:
    data = archivo.read()

data = json.loads(data)

archivo = "archivo.csv"
medias = "medias.csv"

datos_t1 = []
datos_t2 = []
datos_readout_error = []
datos_readout_length = []
datos_prob_01 = []
datos_prob_10 = []

datos_rz1 = []
datos_rz2 = []

datos_x1 = []
datos_x2 = []

datos_sx1 = []
datos_sx2 = []

datos_cnot1 = []
datos_cnot2 = []

for i in data["qubits"]:
   if i[0]['name'] == 'T1':
       datos_t1.append(i[0]['value'])

for i in data["qubits"]:
    if i[1]['name'] == 'T2':
        datos_t2.append(i[1]['value'])

for i in data["qubits"]:
    if i[4]['name'] == 'readout_error':
        datos_readout_error.append(i[4]['value'])

for i in data["qubits"]:
    if i[7]['name'] == 'readout_length':
        datos_readout_length.append(i[7]['value'])

for i in data["qubits"]:
    if i[5]['name'] == 'prob_meas0_prep1':
        datos_prob_01.append(i[5]['value'])

for i in data["qubits"]:
    if i[6]['name'] == 'prob_meas1_prep0':
        datos_prob_10.append(i[6]['value'])

for i in data["gates"]:
    if(i['gate'] == 'rz'):
        datos_rz1.append(i['parameters'][0]['value'])
        datos_rz2.append(i['parameters'][1]['value'])
         
for i in data["gates"]:
    if(i['gate'] == 'x'):
        datos_x1.append(i['parameters'][0]['value'])
        datos_x2.append(i['parameters'][1]['value'])

for i in data["gates"]:
    if(i['gate'] == 'sx'):
        datos_sx1.append(i['parameters'][0]['value'])
        datos_sx2.append(i['parameters'][1]['value'])

for i in data["gates"]:
    if(i['gate'] == 'cx'):
        datos_cnot1.append(i['parameters'][0]['value'])
        datos_cnot2.append(i['parameters'][1]['value'])

print(datos_prob_01)

#Realizar la media cada variable
mediaT1 = sum(datos_t1) / len(datos_t1)
mediaT2 = sum(datos_t2) / len(datos_t2)
mediaReadoutError = sum(datos_readout_error) / len(datos_readout_error)
mediaReadoutLength = sum(datos_readout_length) / len(datos_readout_length)
mediaProb01 = sum(datos_prob_01) / len(datos_prob_01)
mediaProb10 = sum(datos_prob_10) / len(datos_prob_10)
mediaRz = (sum(datos_rz1) + sum(datos_rz2)) / len(datos_rz1)
mediaX = (sum(datos_x1) + sum(datos_x2)) / len(datos_x1)
mediaSx = (sum(datos_sx1) + sum(datos_sx2)) / len(datos_sx1)
mediaCnot = (sum(datos_cnot1) + sum(datos_cnot2)) / len(datos_cnot1)

data = {
    'T1': datos_t1,
    'T2': datos_t2,
    'Readout error': datos_readout_error,
    'Readout lenght': datos_readout_length,
    'Prob 01': datos_prob_01,
    'Prob 10': datos_prob_10,
    'Rz gate error': datos_rz1,
    'Rz gate lenght': datos_rz2,
    'X gate error': datos_x1,
    'X gate lenght': datos_x2,
    'Sx gate error': datos_sx1,
    'Sx gate lenght': datos_sx2,

}

df = pd.DataFrame(data)
print(df)
df.to_csv(archivo, index=False)

data2 = {
    'T1': mediaT1,
    'T2': mediaT2,
    'Readout error': mediaReadoutError,
    'Readout lenght': mediaReadoutLength,
    'Prob 01': mediaProb01,
    'Prob 10': mediaProb10,
    'Rz': mediaRz,
    'X': mediaX,
    'Sx': mediaSx,
    'Cnot': mediaCnot,
}

df2 = pd.DataFrame(data2, index=[0])
print(df2)
df2.to_csv(medias, index=False)


