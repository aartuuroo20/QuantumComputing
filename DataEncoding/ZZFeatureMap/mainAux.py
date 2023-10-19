import numpy as np
import matplotlib.pyplot as plt

from qat.lang import Program, H, X, PH, RY, CNOT
from qat.core import Variable

#Creation of the dataset
num_samples = 20
num_inputs = 2

X_aux = 2 * np.random.rand(num_samples, num_inputs) - 1
y01 = 1 * (np.sum(X_aux, axis=1) >= 0)
y = 2 * y01 - 1 

#Plot of the dataset
for x, y_target in zip(X_aux, y):
    if y_target == 1:
        plt.plot(x[0], x[1], "bo")
    else:
        plt.plot(x[0], x[1], "go")
    plt.plot([-1, 1], [1, -1], "--", color="black")

plt.show()
plt.close()

#Creation of the ZZFeatureMap
qprogram = Program()
nqubits = 2
qubits = qprogram.qalloc(nqubits)

#Dataset variables
ListVarData = []
for i in range(2):
    ListVarData.append(Variable("varData" + str(i)))

#Variational circuit variables
ListVarTheta = []
for i in range(8):
    ListVarTheta.append(Variable("varTheta" + str(i)))


#Creation of the ZZFeatureMap
H(qubits[0])
H(qubits[1])

X(qubits[1])
PH(2*(np.pi - ListVarData[0]) * (np.pi - ListVarData[1]))(qubits[1])
H(qubits[1])
X(qubits[1])

#Creation of variational circuit
RY(ListVarTheta[0])(qubits[0])
RY(ListVarTheta[1])(qubits[1])
CNOT(qubits[0], qubits[1])
RY(ListVarTheta[2])(qubits[0])
RY(ListVarTheta[3])(qubits[1])
CNOT(qubits[0], qubits[1])
RY(ListVarTheta[4])(qubits[0])
RY(ListVarTheta[5])(qubits[1])
CNOT(qubits[0], qubits[1])
RY(ListVarTheta[6])(qubits[0])
RY(ListVarTheta[7])(qubits[1])

#Creation of the circuit and display it
circuit = qprogram.to_circ()
circuit.display()
