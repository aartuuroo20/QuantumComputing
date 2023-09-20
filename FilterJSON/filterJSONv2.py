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
            #Open the json file and load the data in a variable then close the file
            with open(file_input, 'r') as archivo:
                data = json.load(archivo)
            archivo.close()

            #Create the lists that will contain the values of the json file
            #T1 and T2
            T1 = []
            T2 = []

            #Lenght gates
            L_x = []
            L_sx = []
            L_rz = []
            L_cnot = []
            L_readout = []

            #Error gates
            E_x = []
            E_sx = []
            E_rz = []
            E_cnot = []
            E_readout = []

            #Probabilities of the measurements
            prob_01_values = []
            prob_10_values = []

            #Get the values of qubits of the json file
            for qubits in data['qubits']:
                for qubit_data in qubits:
                    if qubit_data['name'] == 'T1':
                        T1.append(qubit_data['value'])
                    elif qubit_data['name'] == 'T2':
                        T2.append(qubit_data['value'])
                    elif qubit_data['name'] == 'readout_error':
                        E_readout.append(qubit_data['value'])
                    elif qubit_data['name'] == 'readout_length':
                        L_readout.append(qubit_data['value'])
                    elif qubit_data['name'] == 'prob_meas0_prep1':
                        prob_01_values.append(qubit_data['value'])
                    elif qubit_data['name'] == 'prob_meas1_prep0':
                        prob_10_values.append(qubit_data['value'])
                    else:
                        pass
            
            #Get the values of gates of the json file
            for gate_data in data['gates']:
                if gate_data['gate'] == 'rz':
                    E_rz.append(gate_data['parameters'][0]['value'])
                    L_rz.append(gate_data['parameters'][1]['value'])
                elif gate_data['gate'] == 'x':
                    E_x.append(gate_data['parameters'][0]['value'])
                    L_x.append(gate_data['parameters'][1]['value'])
                elif gate_data['gate'] == 'sx':
                    E_sx.append(gate_data['parameters'][0]['value'])
                    L_sx.append(gate_data['parameters'][1]['value'])
                elif gate_data['gate'] == 'cx':
                    E_cnot.append(gate_data['parameters'][0]['value'])
                    L_cnot.append(gate_data['parameters'][1]['value'])
                else:
                    pass

            #Calculate the mean of the values
            #T1 and T2
            mean_t1 = us_to_ns(mean(T1)) 
            mean_t2 = us_to_ns(mean(T2))

            #Length gates 
            mean_x_length = mean(L_x)
            mean_rz_length = mean(L_rz)
            mean_sx_length = mean(L_sx)
            mean_cnot_length = mean(L_cnot)
            mean_readoutLenght = mean(L_readout)

            #Error gates
            mean_rz_error = mean(E_rz)
            mean_x_error = mean(E_x)
            mean_sx_error = mean(E_sx)
            mean_cnot_error = mean(E_cnot)
            mean_readoutError = mean(E_readout)

            #Probabilities of the measurements 
            mean_prob01 = mean(prob_01_values)
            mean_prob10 = mean(prob_10_values)
            mean_meas = (mean_prob01 + mean_prob10) / 2

            #Create a dictionary with the means
            means = {
                'T1': mean_t1,
                'T2': mean_t2,
                'E_readout': mean_readoutError,
                'L_readout': mean_readoutLenght,
                'E_meas': mean_meas,
                'E_rz': mean_rz_error,
                'L_rz': mean_rz_length,
                'E_x': mean_x_error,
                'L_x': mean_x_length,
                'E_sx': mean_sx_error,
                'L_sx': mean_sx_length,
                'E_cnot': mean_cnot_error,
                'L_cnot': mean_cnot_length
            }

            #Create a dataframe with the dictionary
            df = pd.DataFrame(means, index=[0])

            #Save the dataframe in a .csv file, if the user doesn't specify a file name and path, the file will be saved as 'means.csv'
            if file_output == None:
                df.to_csv('default_results.csv', index=False)
            else:
                df.to_csv(file_output, index=False)
                file_output.close()
                            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error: {e}")
            return [], []


