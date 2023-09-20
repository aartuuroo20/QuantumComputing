import pandas as pd
from filterJSONv2 import FilterJSON

json_file_name = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
output_file = "C:/Users/a913353/Downloads/meas.csv"

json_object = FilterJSON()
json_object.get_CSV(json_file_name)

#Asignar a cada valor del csv una variable.

if output_file == "" or output_file == None:
    with open("./default_results.csv", 'r') as archivo:
        data = pd.read_csv(archivo)

    t1_mean = data['T1'].mean()
    t2_mean = data['T2'].mean()
    readout_error_mean = data['E_readout'].mean()
    readout_length_mean = data['L_readout'].mean()
    meas_mean = data['E_meas'].mean()

    rz_error_mean = data['E_rz'].mean()
    rz_length_mean = data['L_rz'].mean()
    x_error_mean = data['E_x'].mean()
    x_length_mean = data['L_x'].mean()
    sx_error_mean = data['E_sx'].mean()
    sx_length_mean = data['L_sx'].mean()
    cnot_error_mean = data['E_cnot'].mean()
    cnot_length_mean = data['L_cnot'].mean()

else:
    with open(output_file, 'r') as archivo:
        data = pd.read_csv(archivo)
    
    t1_mean = data['T1'].mean()
    t2_mean = data['T2'].mean()
    readout_error_mean = data['E_readout'].mean()
    readout_length_mean = data['L_readout'].mean()
    meas_mean = data['E_meas'].mean()

    rz_error_mean = data['E_rz'].mean()
    rz_length_mean = data['L_rz'].mean()
    x_error_mean = data['E_x'].mean()
    x_length_mean = data['L_x'].mean()
    sx_error_mean = data['E_sx'].mean()
    sx_length_mean = data['L_sx'].mean()
    cnot_error_mean = data['E_cnot'].mean()
    cnot_length_mean = data['L_cnot'].mean()

    

    
        