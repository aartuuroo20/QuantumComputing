from qat.lang.AQASM import Program, H, PH, RY, CNOT
from qat.lang import qrout, H, CNOT
from qat.core import Variable

import numpy as np
import matplotlib.pyplot as plt

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

#Dataset variables
ListVarData = []
for i in range(2):
    ListVarData.append(Variable("varData" + str(i)))

#Variational circuit variables
ListVarTheta = []
for i in range(8):
    ListVarTheta.append(Variable("varTheta" + str(i)))

#Creation of the ZZFeatureMap
@qrout
def zzfm():
    H(0)
    H(1)
    PH(2* ListVarData[0])(0)
    PH(2* ListVarData[1])(0)
    CNOT(0, 1)
    PH(2*(np.pi - ListVarData[0]) * (np.pi - ListVarData[1]))(1)
    CNOT(0, 1)
    H(0)
    H(1)
    PH(2* ListVarData[0])(0)
    PH(2* ListVarData[1])(0)
    CNOT(0, 1)
    PH(2*(np.pi - ListVarData[0]) * (np.pi - ListVarData[1]))(1)
    CNOT(0, 1)

#Creation of variational circuit
@qrout
def varcircuit():
    RY(ListVarTheta[0])(0)
    RY(ListVarTheta[1])(1)
    CNOT(0, 1)
    RY(ListVarTheta[2])(0)
    RY(ListVarTheta[3])(1)
    CNOT(0, 1)
    RY(ListVarTheta[4])(0)
    RY(ListVarTheta[5])(0)
    CNOT(0, 1)
    RY(ListVarTheta[6])(0)
    RY(ListVarTheta[7])(1)

# Now, create a program and apply the quantum routine to the qubit register
prog = Program()
qbits = prog.qalloc(2)

prog.apply(zzfm, qbits)
prog.apply(varcircuit, qbits)

# Display the circuit
circ = prog.to_circ()
circ.display()