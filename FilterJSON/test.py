import json
import pandas as pd
from filterJSONv2 import FilterJSON

json_file_name = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
output_file = "C:/Users/a913353/Downloads/means.csv"

json_object = FilterJSON()
json_object.get_CSV(json_file_name)

#Asignar a cada valor del csv una variable.

with open(output_file, 'r') as archivo:
    data = pd.read_csv(archivo)

t1_mean = data['T1'].mean()
t2_mean = data['T2'].mean()
readout_error_mean = data['readout_error'].mean()
readout_length_mean = data['readout_length'].mean()
meas_mean = data['meas'].mean()

rz_error_mean = data['RZ_error'].mean()
rz_length_mean = data['RZ_length'].mean()
x_error_mean = data['X_error'].mean()
x_length_mean = data['X_length'].mean()
sx_error_mean = data['Sx_error'].mean()
sx_length_mean = data['Sx_length'].mean()
cnot_error_mean = data['CNOT_error'].mean()
cnot_length_mean = data['CNOT_length'].mean()

    
        