import json
import pandas as pd

class FilterJSON:
    
    #Method that return a .csv file with the mean of the values of the json file
    def get_CSV(self, file_input, file_output = None):

        #Function that calculate the mean of a list
        def mean(lista):
            mean = sum(lista) / len(lista)
            return mean
        
        #Function that convert the values of T1 and T2 from us to ns
        def us_to_ns(mean):
            mean = mean * 1000
            return mean
        try:
            #Open the json file
            with open(file_input, 'r') as archivo:
                data = json.load(archivo)

            #Create the lists that will contain the values of the json file
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

            #Get the values of qubits of the json file
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
            
            #Get the values of gates of the json file
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

            #Calculate the mean of the values
            mean_t1 = us_to_ns(mean(t1_values)) 
            mean_t2 = us_to_ns(mean(t2_values))
            mean_readoutError = mean(readout_error_values)
            mean_readoutLenght = mean(readout_length_values)
            mean_prob01 = mean(prob_01_values)
            mean_prob10 = mean(prob_10_values)
            mean_meas = (mean_prob01 + mean_prob10) / 2

            mean_rz_error = mean(rz_error_values)
            mean_rz_length = mean(rz_length_values)
            mean_x_error = mean(x_error_values)
            mean_x_length = mean(x_length_values)
            mean_sx_error = mean(sx_error_values)
            mean_sx_length = mean(sx_length_values)
            mean_cnot_error = mean(cnot_error_values)
            mean_cnot_length = mean(cnot_length_values)

            #Create a dictionary with the means
            means = {
                'T1': mean_t1,
                'T2': mean_t2,
                'readout_error': mean_readoutError,
                'readout_length': mean_readoutLenght,
                'meas': mean_meas,
                'RZ_error': mean_rz_error,
                'RZ_length': mean_rz_length,
                'X_error': mean_x_error,
                'X_length': mean_x_length,
                'Sx_error': mean_sx_error,
                'Sx_length': mean_sx_length,
                'CNOT_error': mean_cnot_error,
                'CNOT_length': mean_cnot_length
            }

            #Create a dataframe with the dictionary
            df = pd.DataFrame(means, index=[0])

            #Save the dataframe in a .csv file, if the user doesn't specify a file name and path, the file will be saved as 'means.csv'
            if file_output == None:
                df.to_csv('means.csv', index=False)
            else:
                df.to_csv(file_output, index=False)
                            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")
            return [], []


