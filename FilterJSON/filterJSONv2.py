import json
import pandas as pd

class FilterJSON:

    def getCSV(file_input):

        try:
            
            with open(file_input, 'r') as archivo:
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

                data = {
                    'T1': t1_values,
                    'T2': t2_values,
                    'readout_error': readout_error_values,
                    'readout_length': readout_length_values,
                    'prob_meas0_prep1': prob_01_values,
                    'prob_meas1_prep0': prob_10_values,
                    'rz_error': rz_error_values,
                    'rz_length': rz_length_values,
                    'x_error': x_error_values,
                    'x_length': x_length_values,
                    'sx_error': sx_error_values,
                    'sx_length': sx_length_values,
                    'cnot_error': cnot_error_values,
                    'cnot_length': cnot_length_values,
                }

                df = pd.DataFrame(data)
                df.to_csv('data.csv', index=False)
                
                '''
                mean_t1 = mean(t1_values)
                mean_t2 = mean(t2_values)
                mean_readoutError = mean(readout_error_values)
                mean_readoutLenght = mean(readout_length_values)
                mean_prob01 = mean(prob_01_values)
                mean_prob10 = mean(prob_10_values)

                mean_rz = mean(rz_error_values, rz_length_values)
                mean_x = mean(x_error_values, x_length_values)
                mean_sx = mean(sx_error_values, sx_length_values)
                mean_cnot = mean(cnot_error_values, cnot_length_values)

                means = {
                    'T1': mean_t1,
                    'T2': mean_t2,
                    'readout_error': mean_readoutError,
                    'readout_length': mean_readoutLenght,
                    'prob_meas0_prep1': mean_prob01,
                    'prob_meas1_prep0': mean_prob10,
                    'RZ': mean_rz,
                    'X': mean_x,
                    'Sx': mean_sx,
                    'CNOT': mean_cnot,
                }

                df2 = pd.DataFrame(means, index=[0])
                print(df2)
                df2.to_csv('means.csv', index=False)
                '''
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")
            return [], []

    '''
    @staticmethod  
    def mean(lista, opcional_lista = []):
        mean = (sum(lista) + sum(opcional_lista))/ len(lista)
        return mean
    '''

