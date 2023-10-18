import numpy as np
import matplotlib.pyplot as plt

from qat.lang import Program, H, X, PH, RY, CSIGN, RZ
from qat.core import Variable

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

varData0 = Variable("varData0")
varData1 = Variable("varData1")

H(qubits[0])
H(qubits[1])

X(qubits[1])
PH(2*(np.pi - varData0) * (np.pi - varData1))(qubits[1])
H(qubits[1])
X(qubits[1])

#Creation of variational circuit

var0 = Variable("var0")
var1 = Variable("var1")
var2 = Variable("var2")
var3 = Variable("var3")
var4 = Variable("var4")
var5 = Variable("var5")
var6 = Variable("var6")
var7 = Variable("var7")
var8 = Variable("var8")
var9 = Variable("var9")
var10 = Variable("var10")
var11 = Variable("var11")

RY(var0)(qubits[0])
RY(var1)(qubits[1])
RZ(var2)(qubits[0])
RZ(var3)(qubits[1])
CSIGN(qubits[0], qubits[1])
RY(var4)(qubits[0])
RY(var5)(qubits[1])
RZ(var6)(qubits[0])
RZ(var7)(qubits[1])
CSIGN(qubits[0], qubits[1])
RY(var8)(qubits[0])
RY(var9)(qubits[1])
RZ(var10)(qubits[0])
RZ(var11)(qubits[1])

#Creation of the circuit and display it
circuit = qprogram.to_circ()
circuit.display()
