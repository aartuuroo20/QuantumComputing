import json
import pandas as pd

class FilterJSON:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo


    def filter(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                data = json.load(archivo)

            t1_values = []
            t2_values = []
            readout_error_values = []
            readout_length_values = []
            prob_01_values = []
            prob_10_values = []

            rz_error_values = []
            rz_length_values = []
            x_error_values = []
            x_length_values = []
            sx_error_values = []
            sx_length_values = []
            cnot_error_values = []
            cnot_length_values = []

            for qubits in data['qubits']:
                for qubit_data in qubits:
                    if qubit_data['name'] == 'T1':
                        t1_values.append(qubit_data['value'])
                    elif qubit_data['name'] == 'T2':
                        t2_values.append(qubit_data['value'])
                    elif qubit_data['name'] == 'readout_error':
                        readout_error_values.append(qubit_data['value'])
                    elif qubit_data['name'] == 'readout_length':
                        readout_length_values.append(qubit_data['value'])
                    elif qubit_data['name'] == 'prob_meas0_prep1':
                        prob_01_values.append(qubit_data['value'])
                    elif qubit_data['name'] == 'prob_meas1_prep0':
                        prob_10_values.append(qubit_data['value'])
                    else:
                        pass
        
            for gate_data in data['gates']:
                if gate_data['gate'] == 'rz':
                    rz_error_values.append(gate_data['parameters'][0]['value'])
                    rz_length_values.append(gate_data['parameters'][1]['value'])
                elif gate_data['gate'] == 'x':
                    x_error_values.append(gate_data['parameters'][0]['value'])
                    x_length_values.append(gate_data['parameters'][1]['value'])
                elif gate_data['gate'] == 'sx':
                    sx_error_values.append(gate_data['parameters'][0]['value'])
                    sx_length_values.append(gate_data['parameters'][1]['value'])
                elif gate_data['gate'] == 'cx':
                    cnot_error_values.append(gate_data['parameters'][0]['value'])
                    cnot_length_values.append(gate_data['parameters'][1]['value'])
                else:
                    pass

            return t1_values, t2_values, readout_error_values, readout_length_values, prob_01_values, prob_10_values, rz_error_values, rz_length_values, x_error_values, x_length_values, sx_error_values, sx_length_values, cnot_error_values, cnot_length_values

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")
            return [], []
        
    def mean(lista):
        mean = sum(lista) / len(lista)
        return mean

json_file_name = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
file_data = "data.csv"
file_means = "means.csv"

json1 = FilterJSON(json_file_name)
t1_values, t2_values, readout_error_values, readout_length_values, prob_01_values, prob_10_values, rz_error_values, rz_length_values, x_error_values, x_length_values, sx_error_values, sx_length_values, cnot_error_values, cnot_length_values = json1.filter(json_file_name)

data = {
    'T1': t1_values,
    'T2': t2_values,
    'readout_error': readout_error_values,
    'readout_length': readout_length_values,
    'prob_meas0_prep1': prob_01_values,
    'prob_meas1_prep0': prob_10_values,
    'rz_error': rz_error_values,
    'x_error': x_error_values,
    'x_length': rz_length_values,
    'sx_error': sx_error_values,
    'sx_length': sx_length_values,
}

df = pd.DataFrame(data)
print(df)
df.to_csv(file_data, index=False)

'''

mediaT1 = mean(t1_values)
mediaT2 = mean(t2_values)
mediaReadoutError = mean(readout_error_values)
mediaReadoutLength = mean(readout_length_values)
mediaProb01 = mean(prob_01_values)
mediaProb10 = mean(prob_10_values)
mediaRzError = mean(rz_error_values)
mediaRzLength = mean(rz_length_values)
mediaXError = mean(x_error_values)
mediaXLength = mean(x_length_values)
mediaSxError = mean(sx_error_values)
mediaSxLength = mean(sx_length_values)
mediaCnotError = mean(cnot_error_values)
mediaCnotLength = mean(cnot_length_values)

means = {
    'T1': mediaT1,
    'T2': mediaT2,
    'readout_error': mediaReadoutError,
    'readout_length': mediaReadoutLength,
    'prob_meas0_prep1': mediaProb01,
    'prob_meas1_prep0': mediaProb10,
    'rz_error': mediaRzError,
    'rz_length': mediaRzLength,
    'x_error': mediaXError,
    'x_length': mediaXLength,
    'sx_error': mediaSxError,
    'sx_length': mediaSxLength,
    'cnot_error': mediaCnotError,
    'cnot_length': mediaCnotLength
}

df2 = pd.DataFrame(means, index=[0])
print(df2)
df2.to_csv(file_means, index=False)

'''
