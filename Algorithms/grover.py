from qat.lang.AQASM import Program, H, X, CNOT, Z, QRoutine
from qat.qpus import get_default_qpu
import numpy as np

#Creamos el difusor
def diffusor(nqubits):
    routine = QRoutine()
    wires = routine.new_wires(2 * nqubits)
    for wire in wires:
        H(wire)
        X(wire)
    Z.ctrl(2 * nqubits - 1)(wires)     
    for wire in wires:
        X(wire)
        H(wire)
    return routine

def is_Palindrome(nqubits): #No entiendo muy bien como funciona
    routine = QRoutine()
    first_half = routine.new_wires(nqubits)
    second_half = routine.new_wires(nqubits)
    for w1, w2 in zip(first_half, reversed(second_half)):
        CNOT(w1, w2)
    for w2 in second_half:
        X(w2)
    Z.ctrl(nqubits - 1)(second_half)
    return routine

qprogram = Program()

nqubits = 2 #Numbero de qubits
qubits=qprogram.qalloc(nqubits * 2) #Reservamos en memoria el numero de estados
difusor = diffusor(nqubits) #Creamos el difusor
oracle = is_Palindrome(nqubits) #Creamos el oraculo

#Aplicamos la puerta H a todos los qubits
H(qubits[0]) 
H(qubits[1]) 
H(qubits[2]) 
H(qubits[3]) 

#Calculamos el numero de iteraciones optimas
nsteps = int(np.pi * np.sqrt(2 ** nqubits) / 4)
print("Number of steps: %d" % nsteps)
for i in range(nsteps):
    oracle(qubits)
    difusor(qubits)

circuit = qprogram.to_circ()
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

circuit.display()



