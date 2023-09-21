import pandas as pd
from filterJSONv2 import FilterJSON

json_file_name = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"
output_file = "C:/Users/a913353/Downloads/meas.csv"

json_object = FilterJSON()
json_object.get_CSV(json_file_name)

#Asignar a cada valor del csv una variable.

if output_file == "" or output_file == None:
    output_file = "./default_results.csv"

with open(output_file, 'r') as archivo:
    data = pd.read_csv(archivo)
archivo.close()

#T1 and T2
T1 = data['T1'].mean()
T2 = data['T2'].mean()

#Lenght gates
L_readout = data['L_readout'].mean()
L_rz = data['L_rz'].mean()
L_x = data['L_x'].mean()
L_sx = data['L_sx'].mean()
L_cnot = data['L_cnot'].mean()

#Error gates
E_readout = data['E_readout'].mean()
E_meas = data['E_meas'].mean()
E_rz = data['E_rz'].mean()
E_x = data['E_x'].mean()
E_sx = data['E_sx'].mean()
E_cnot = data['E_cnot'].mean()

    

    
        