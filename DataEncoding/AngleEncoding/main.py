import numpy as np
import matplotlib.pyplot as plt

from qat.lang import Program, RY
from qat.qpus import get_default_qpu

#Creation of the circuit
qprogram = Program()
nqubits = 2
qubits = qprogram.qalloc(nqubits)

RY(np.pi)(qubits[0])
RY(2*np.pi)(qubits[1])

#Execution of the circuit
circuit = qprogram.to_circ()
job = circuit.to_job()
result = get_default_qpu().submit(job)

#Creation of the list of states and probabilities and printing results
states = []
probs = []

for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))
    states.append(sample.state)
    probs.append(sample.probability)

#Creation of the histogram of states and probabilities
plt.figure()
plt.bar(str(states), probs)
plt.xlabel('Estados')
plt.ylabel('Probabilidades')
plt.title('Histograma de Estados y Probabilidades')
plt.show()
plt.close()

#Display of the circuit
circuit.display()

