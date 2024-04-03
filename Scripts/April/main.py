import pandas as pd

filename = 'C:/Users/a913353/OneDrive - Eviden/Desktop/final_results_completo error_correctiond2_n5_250324.xlsx'

df = pd.read_excel( filename, 
                   sheet_name='error_correctiond3_n5_00000')
output = 'final_results5.csv'

estados = []
valores = []
probabilidad = []
executionTime = []
comprobacion = ['00000', '11000', '10100', '01100', '10010', '01010', '00110', '11110', 
                '10001', '01001', '00101', '11101', '00011', '11011', '10111', '01111']

tamano_bloque = 32
total_bloques = 10

for i in range(total_bloques):  # Repetir 10 veces
    inicio = 3 + i * tamano_bloque
    fin = 35 + i * tamano_bloque  # El primer bloque va hasta la fila 35

   # Tomar los siguientes 32 elementos en cada iteración
    bloque32 = df.iloc[inicio:fin]
    
    probabilidad = bloque32['Unnamed: 11'].tolist()
    estados = bloque32['Unnamed: 3'].tolist()
    resultados = list(zip(estados, probabilidad))

    resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)

    top16 = resultados_ordenados[:16]
    coincidencias = [estado for estado in top16 if estado[0] in comprobacion]

    print("Iteración:", i + 1)
    print("Estados coincidentes con la lista de comprobación:")
    '''
    for coincidencia in coincidencias:
        print(coincidencia)
    '''

    contador_coincidencias = sum(1 for estado in top16 if estado[0] in comprobacion)
    print("Número de estados coincidentes con la lista de comprobación:", contador_coincidencias)
    probabilidad_final = (contador_coincidencias / 16)
    print("Probabilidad de aciertos:", probabilidad_final)
    print()

