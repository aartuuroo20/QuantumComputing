import pandas as pd

df = pd.read_csv('C:/Users/a913353/OneDrive - ATOS/Desktop/ibm_perth/prueba/error_correctiond3_n5_00000_ibm_perth_Thermal_relaxation.csv', sep=';')
output = 'final_results5.csv'

valores = []
executionTime = []
'''
comprobacion = ['0000000', '1100000', '1010000', '0110000', '1001000', '0101000', '0011000', '1111000',
                '1000100', '0100100', '0010100', '1110100', '0001100', '1101100', '1011100', '0111100']
'''

comprobacion = [0, 11, 101, 110, 1001, 1010, 1100, 1111, 
                10001, 10010, 10100, 10111, 11000, 11011, 11101, 11110]

primeras_128_filas = df.head(32)
print(primeras_128_filas)

probabilidad = primeras_128_filas['Probability'].tolist()
estados = primeras_128_filas['State'].tolist()
resultados = list(zip(estados, probabilidad))

resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)
top16 = resultados_ordenados[:16]

print ("Top 32:")
for resultado in resultados:
    print(resultado)

print("Top 16:")
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


