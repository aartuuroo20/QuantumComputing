from qat.lang import Program, X, AbstractGate
import numpy as np
from test.test import Test

test = Test()

def matrix_gen():
    return np.array([[1, 0], [1, 1]])

qprogram = Program()
nquibts = 2
qubits = qprogram.qalloc(nquibts)

X(qubits[0])
my_gate = AbstractGate("my_gate", [], arity=1, matrix_generator=test.create())
my_gate()(qubits[1])

circuit = qprogram.to_circ()
circuit.display()



