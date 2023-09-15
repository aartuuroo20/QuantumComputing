import json
import pandas as pd

ruta_archivo = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
with open(ruta_archivo, "r") as archivo:
    data = archivo.read()

data = json.loads(data)

archivo = "archivo.csv"
medias = "medias.csv"

for i in range(len(data['qubits'])):
    datos_t1 = list(map(lambda y: y[i]['value'], filter(lambda x: x[i]['name'] == 'T1', data['qubits'])))

datos_t2 = list(map(lambda y: y[1]['value'], filter(lambda x: x[1]['name'] == 'T2', data['qubits'])))
datos_readout_error = list(map(lambda y: y[4]['value'], filter(lambda x: x[4]['name'] == 'readout_error', data['qubits'])))
datos_readout_length = list(map(lambda y: y[7]['value'], filter(lambda x: x[7]['name'] == 'readout_length', data['qubits'])))
datos_prob_01 = list(map(lambda y: y[5]['value'], filter(lambda x: x[5]['name'] == 'prob_meas0_prep1', data['qubits'])))
datos_prob_10 = list(map(lambda y: y[6]['value'], filter(lambda x: x[6]['name'] == 'prob_meas1_prep0', data['qubits'])))

datos_rz_error = list(map(lambda y: y['parameters'][0]['value'], filter(lambda x: x['gate'] == 'rz', data['gates'])))
datos_rz_length = list(map(lambda y: y['parameters'][1]['value'], filter(lambda x: x['gate'] == 'rz', data['gates'])))
datos_x_error = list(map(lambda y: y['parameters'][0]['value'], filter(lambda x: x['gate'] == 'x', data['gates'])))
datos_x_length = list(map(lambda y: y['parameters'][1]['value'], filter(lambda x: x['gate'] == 'x', data['gates'])))
datos_sx_error = list(map(lambda y: y['parameters'][0]['value'], filter(lambda x: x['gate'] == 'sx', data['gates'])))
datos_sx_length = list(map(lambda y: y['parameters'][1]['value'], filter(lambda x: x['gate'] == 'sx', data['gates'])))
datos_cnot_error = list(map(lambda y: y['parameters'][0]['value'], filter(lambda x: x['gate'] == 'cx', data['gates'])))
datos_cnot_length = list(map(lambda y: y['parameters'][1]['value'], filter(lambda x: x['gate'] == 'cx', data['gates'])))

datos = {
    'T1': datos_t1,
    'T2': datos_t2,
    'readout_error': datos_readout_error,
    'readout_length': datos_readout_length,
    'prob_meas0_prep1': datos_prob_01,
    'prob_meas1_prep0': datos_prob_10,
    'rz_error': datos_rz_error,
    'x_error': datos_x_error,
    'x_length': datos_rz_length,
    'sx_error': datos_sx_error,
    'sx_length': datos_sx_length
}

df = pd.DataFrame(datos)

df.to_csv(archivo, index=False)

mediaT1 = sum(datos_t1) / len(datos_t1)
mediaT2 = sum(datos_t2) / len(datos_t2)
mediaReadoutError = sum(datos_readout_error) / len(datos_readout_error)
mediaReadoutLength = sum(datos_readout_length) / len(datos_readout_length)
mediaProb01 = sum(datos_prob_01) / len(datos_prob_01)
mediaProb10 = sum(datos_prob_10) / len(datos_prob_10)

mediaRz = (sum(datos_rz_error) + sum(datos_readout_length)) / len(datos_rz_error)
mediaX = (sum(datos_x_error) + sum(datos_x_length)) / len(datos_x_error)
mediaSx = (sum(datos_sx_error) + sum(datos_sx_length)) / len(datos_sx_error)
mediaCnot = (sum(datos_cnot_error) + sum(datos_cnot_length)) / len(datos_cnot_error)

datos2 = {
    'T1': [mediaT1],
    'T2': [mediaT2],
    'readout_error': [mediaReadoutError],
    'readout_length': [mediaReadoutLength],
    'prob_meas0_prep1': [mediaProb01],
    'prob_meas1_prep0': [mediaProb10],
    'Rz': [mediaRz],
    'X': [mediaX],
    'Sx': [mediaSx],
    'Cnot': [mediaCnot]
}

df2 = pd.DataFrame(datos2, index=[0])
df2.to_csv(medias, index=False)








