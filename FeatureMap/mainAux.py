import numpy as np
import matplotlib.pyplot as plt

from qat.lang import Program, H, X, PH, RY, CSIGN, RZ

#Creation of the dataset
num_samples = 20
num_inputs = 2

X_aux = 2 * np.random.rand(num_samples, num_inputs) - 1
y01 = 1 * (np.sum(X_aux, axis=1) >= 0)
y = 2 * y01 - 1 

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

H(qubits[0])
H(qubits[1])

X(qubits[1])
PH(2*(np.pi - X_aux[0][0]) * (np.pi - X_aux[0][1]))(qubits[1])
H(qubits[1])
X(qubits[1])

#Creation of variational circuit
'''
theta = []
for i in range(12):
    theta.append(qprogram.new_var(float, '\\theta'))
'''
theta = qprogram.new_var(float, '\\theta')

RY(theta)(qubits[0])
RY(theta)(qubits[1])
RZ(theta)(qubits[0])
RZ(theta)(qubits[1])
CSIGN(qubits[0], qubits[1])
RY(theta)(qubits[0])
RY(theta)(qubits[1])
RZ(theta)(qubits[0])
RZ(theta)(qubits[1])
CSIGN(qubits[0], qubits[1])
RY(theta)(qubits[0])
RY(theta)(qubits[1])
RZ(theta)(qubits[0])
RZ(theta)(qubits[1])

#Creation of the circuit and display it
circuit = qprogram.to_circ()
circuit.display()

