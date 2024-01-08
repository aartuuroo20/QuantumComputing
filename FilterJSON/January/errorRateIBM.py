import pandas as pd

df = pd.read_csv('C:/Users/a913353/OneDrive - ATOS/Desktop/ibm_perth/error_correctiond3_n5/simulacion_ibm_perth_00000.csv', sep=';')
output = 'final_results5.csv'

estados = []
valores = []
probabilidad = []
executionTime = []
comprobacion = ['00000', '00011', '00101', '00110', '01001', '01010', '01100', '01111', 
                '10001', '10010', '10100', '10111', '11000', '11011', '11101', '11110']


primera_fila = df.loc[6, 'State: probability']

for state, value in zip(primera_fila.split(','), primera_fila.split(',')):
    estado_substring = state[state.find("'")+1: state.find(':')-1]
    estados.append(estado_substring)

    valor_substring = value[value.find(':')+1:].strip()
    valores.append(valor_substring)

if valores:
    valores[-1] = valores[-1][:-1]

valores = [int(cadena) for cadena in valores]

for value in valores:
    probabilidad.append(value/8192)

# Unir cada elemento con su posición equivalente
resultados = list(zip(estados, valores, probabilidad))
resultados_ordenados = sorted(resultados, key=lambda x: x[2], reverse=True)
top16 = resultados_ordenados[:16]

for resultado in top16:
    print(resultado)

# Comparar los estados de top 16 con la lista de comprobación
coincidencias = [estado for estado in top16 if estado[0] in comprobacion]

print("Estados coincidentes con la lista de comprobación:")
for coincidencia in coincidencias:
    print(coincidencia)

contador_coincidencias = sum(1 for estado in top16 if estado[0] in comprobacion)
print("Número de estados coincidentes con la lista de comprobación:", contador_coincidencias)
probabilidad_final = (contador_coincidencias/16)
print("Probabilidad de aciertos:", probabilidad_final)

for time in df['Execution time (s)']:
    print(type(time))
    executionTime.append(time)

file = pd.DataFrame({'Ejecucicon': executionTime})
file.to_csv(output, mode='w', encoding='utf-8', index=False, float_format='%.0f')









