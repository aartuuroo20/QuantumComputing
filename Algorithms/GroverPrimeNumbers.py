from numpy import *
import math
from qat.lang.AQASM import Program, H, X, Z, QRoutine, CustomGate
from qat.qpus import get_default_qpu

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = zeros((filas, columnas))

    def print_matriz(self):
        print(self.matriz)

    def cubrir_diagonal(self):
        for i in range(len(self.matriz)):
            if i in lista:
                self.matriz[i][i] = -1
            else:
                self.matriz[i][i] = 1

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

matriz = Matriz(numero, numero) #Inicializamos la matriz con ceros de tamaño numero x numero
matriz.print_matriz() #Imprimimos la matriz con ceros

matriz.cubrir_diagonal() #Cubrimos la diagonal de la matriz con -1 y 1

matriz_primos = CustomGate(matriz.matriz) #Creamos una puerta personalizada con la matriz para poder operar
matriz.print_matriz() #Imprimimos la matriz con -1 y 1

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

m = len(lista)
n = numero
print("Numero de soluciones: %d" % m)
k = int(math.pi / (4 * arccos(sqrt(1 - m / n))))
print("Numero de iteraciones: %d" % k)

probabilidad = sin((2 * k + 1) * arccos(sqrt((n - m) / n)))**2
print("Probabilidad de encontrar la solucion: %f" %probabilidad)

qprog = Program()
nqbits = qprog.qalloc(qubits)

difusor = diffusor(qubits)
oracle = oraculo(qubits, matriz_primos)

for qbit in nqbits:
    H(qbit)

for _ in range(k):
    oracle(nqbits)
    difusor(nqbits)
    
circuit = qprog.to_circ()
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

circuit.display()












