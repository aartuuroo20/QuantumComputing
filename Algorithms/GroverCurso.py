from numpy import *
import math
from qat.lang.AQASM import *
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

matriz = zeros((numero,numero))
print(matriz)

for i in range(len(matriz)):
    if i in lista:
        matriz[i][i] = -1
    else: 
        matriz[i][i] = 1

print(matriz)

def oraculo(k, matriz):
    routine = QRoutine()
    wires = routine.new_wires(k)
    matriz(wires)
    return routine

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







