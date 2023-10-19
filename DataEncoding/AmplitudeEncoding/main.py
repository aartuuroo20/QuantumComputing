import numpy as np

from qat.lang import Program, AbstractGate
from matrix import Matrix

matrix = Matrix()

qprogram = Program()
nqubits = 3
qubits = qprogram.qalloc(nqubits)

amplitude = AbstractGate("amplitude", [], arity=3, matrix_generator=matrix.genMatrix())
amplitude()(qubits[0], qubits[1], qubits[2])

circuit = qprogram.to_circ()
circuit.display()