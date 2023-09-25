import pandas as pd
from filterJSONv2 import FilterJSON

#Paths of json and output files
json_file_name = "write path of json file"
output_file = "write path of output file"

json_object = FilterJSON()
file_path = json_object.get_CSV(json_file_name)

#Open the json file and load the data in a variable then close the file
with open(file_path, 'r') as archivo:
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

    

    
        