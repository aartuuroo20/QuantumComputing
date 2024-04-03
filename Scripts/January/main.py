import pandas as pd

file_path = 'C:/Users/a913353/OneDrive - ATOS/Desktop/ibm_perth/adder_n4/simulacion_ibm_perth_000.csv'
output = 'final_results5.csv'

data = pd.read_csv(file_path, sep=';')

values1 = []
probabilities1 = []
executionTime = []

for state in data['State: probability']:
    if state.find('1011') != -1:
        encontrado = state.find('1011')
        substring = state[state.find(':', encontrado)+1:state.find(',', encontrado)]
        values1.append(substring)

for value in values1:
    probabilities1.append(int(value)/8192)

for time in data['Execution time (s)']:
    print(type(time))
    executionTime.append(time)

print(type(executionTime))
print(executionTime)

file = pd.DataFrame({'Ejecucicon': executionTime})
print(file)
file.to_csv(output, mode='w', encoding='utf-8', index=False, float_format='%.0f')





        
    

        

