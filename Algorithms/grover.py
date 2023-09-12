#El funcionamiento del algoritmo de Grover trata de buscar elementos sobre una lista no estructurada de N elementos,
#aplicamos puerta hadamard para crear una superposicion de estados, creamos el oracle que identifica la solucion correcta cambiandole el signo,
#aplicamos un difusor que cambia la amplitud de las soluciones correctas para aumentar la probabilidad de encontrarlas disminuyendo el resto.

from qat.lang.AQASM import Program, H, X, CNOT, Z, QRoutine
from qat.qpus import get_default_qpu
import numpy as np

#Creamos el difusor el cual cambia la amplitud de las soluciones correctas para aumentar a prob de encontrarlas
def diffusor(k):
    routine = QRoutine() #Creamos una rutina cuantica la cual nos permite crear puertas abstractas (puertas personalizadas) y creara la "caja"
    wires = routine.new_wires(2 * k) # Creamos una lista de cables de tamaño 2*nqubits (4)
    for wire in wires: #Aplicamos la puerta H y una puerta X a todos los cables
        H(wire)
        X(wire)
    Z.ctrl(2 * k - 1)(wires) #Aplicamos la puerta Z controlada a todos los cables la cual amplia la amplitud de las soluciones correctas. En todos los cables aplicar puerta CZ
    for wire in wires: #Aplicamos la puerta X y una puerta H a todos los cables
        X(wire)
        H(wire)
    return routine

#Creamos el oraculo el cual que verifica si la solucion es correcta donde cambiamos el signo de la solucion correcta.
def is_Palindrome(k): 
    routine = QRoutine()
    first_half = routine.new_wires(k) #Creamos una primera lista de cables de tamaño nqubits (2) la cual almacena la primera mitad de la cadena
    second_half = routine.new_wires(k) #Creamos una segunda lista de cables de tamaño nqubits (2) la cual almacena la segunda mitad de la cadena
    with routine.compute():
        #zip asigna a cada elemento de la primera lista el elemento de la segunda lista y reverses invierte el orden de la segunda lista
        for w1, w2 in zip(first_half, reversed(second_half)): #Itera sobre los pares de quibits de la primera y segunda lista, combina los dos y los invierte correspondiendo al mismo indice
            CNOT(w1, w2)
        for w2 in second_half: #Aplicamos una puerta X invirtiendo el estado identificando los estados incorrectos debio a que se espera que ambos sean iguales
            X(w2)
    Z.ctrl(k - 1)(second_half) #Aplicamos la puerta Z controlada a la segunda lista de cables la cual cambia de signo la amplitud de las soluciones incorrectas 
    routine.uncompute()
    return routine

#Creamos el programa
qprogram = Program()

k = 2 
qubits=qprogram.qalloc(k * 2) #Reservamos en memoria el numero de estados y asignamos numero qubits
difusor = diffusor(k) #Creamos el difusor
oracle = is_Palindrome(k) #Creamos el oraculo

#Aplicamos la puerta H a todos los qubits
H(qubits[0]) 
H(qubits[1]) 
H(qubits[2]) 
H(qubits[3]) 

#Calculamos el numero de iteraciones optimas
nsteps = int(np.pi * np.sqrt(2 ** k) / 4)
print("Number of steps: %d" % nsteps)

#Aplicamos el algoritmo de Grover
for i in range(nsteps):
    oracle(qubits)
    difusor(qubits)

# Exportamos este programa a un circuito cuántico
circuit = qprogram.to_circ()

# Creamos un job
job = circuit.to_job()

#Creamos una unidad de proceso cuántico y enviamos el job a la QPU
result = get_default_qpu().submit(job)

#Mostramos los resultados
for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

#Mostramos el circuito
circuit.display()