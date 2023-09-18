import json
import pandas as pd
from filterJSONv2 import FilterJSON

json_file_name = "C:/Users/a913353/Downloads/perth_3_8_23_H_18.json"

json1 = FilterJSON()
json1.getCSV(json_file_name)

'''
t1_values, t2_values, readout_error_values, readout_length_values, prob_01_values, prob_10_values, rz_error_values, rz_length_values, x_error_values, x_length_values, sx_error_values, sx_length_values, cnot_error_values, cnot_length_values = json1.filter()

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

mean_t1 = json1.mean(t1_values)
mean_t2 = json1.mean(t2_values)
mean_readoutError = json1.mean(readout_error_values)
mean_readoutLenght = json1.mean(readout_length_values)
mean_prob01 = json1.mean(prob_01_values)
mean_prob10 = json1.mean(prob_10_values)

mean_rz = json1.mean(rz_error_values, rz_length_values)
mean_x = json1.mean(x_error_values, x_length_values)
mean_sx = json1.mean(sx_error_values, sx_length_values)
mean_cnot = json1.mean(cnot_error_values, cnot_length_values)

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
df2.to_csv(file_means, index=False)

'''

