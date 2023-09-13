from numpy import *
import math
from qat.lang.AQASM import Program, H, X, Z, QRoutine, CustomGate
from qat.qpus import get_default_qpu

qubits = 4
numero = 2**qubits
lista = []
# Recorre todos los números hasta n y almacena los números primos en una lista
for num in range(numero):
   # Todos los números primos son mayores que 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           lista.append(num)

print(lista)

matriz = zeros((numero,numero)) #Inicializamos la matriz con ceros de tamaño numero x numero
print(matriz) #Imprimimos la matriz de todo 0

for i in range(len(matriz)): #Recorremos la diagonal de la matriz
    if i in lista: #Comprobamos si el numero es primo comrpobando si esta en la lista
        matriz[i][i] = -1 #Si es primo cambiamos a -1
    else: 
        matriz[i][i] = 1 #Si no es primo no cambiamos a 1

matriz_primos = CustomGate(matriz) #Creamos una puerta personalizada con la matriz para poder operar
print(matriz) #Imprimimos la matriz con los valores cambiados

#Definimos el oracle 
def oraculo(k, matriz_primos):
    routine = QRoutine()
    wires = routine.new_wires(k)
    matriz_primos(wires)
    return routine

#Definimos el difusor
def diffusor(k):
    routine = QRoutine()
    wires = routine.new_wires(k)
    with routine.compute():
        for wire in wires:
            H(wire)
            X(wire)
    Z.ctrl(k - 1)(wires)
    routine.uncompute()
    return routine

numeroSoluciones = len(lista)
print("Numero de soluciones: %d" % numeroSoluciones)
numeroIteraciones = int(math.pi / (4 * arccos(sqrt(1 - numeroSoluciones / numero))))
print("Numero de iteraciones: %d" % numeroIteraciones)

probabilidad = sin((2 * numeroIteraciones + 1) * arccos(sqrt((numero - numeroSoluciones) / numero)))**2
print("Probabilidad de encontrar la solucion: %f" %probabilidad)

qprog = Program()
nqbits = qprog.qalloc(qubits)

difusor = diffusor(qubits)
oracle = oraculo(qubits, matriz_primos)

for qbit in nqbits:
    H(qbit)

for _ in range(numeroIteraciones):
    oracle(nqbits)
    difusor(nqbits)
    
circuit = qprog.to_circ()
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

circuit.display()












