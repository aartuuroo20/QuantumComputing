import numpy as np

from qat.lang import Program, AbstractGate
from qat.qpus import get_default_qpu, PyLinalg

from matrix import Matrix

def genMatrix():
    a = [[1,0,0,0],
         [0,1,0,0],
         [0,0,1,0],
         [0,0,0,1]]

qprogram = Program()
nqubits = 3
qubits = qprogram.qalloc(nqubits)

amplitude = AbstractGate("amplitude", [], arity=3, matrix_generator=matrix.genMatrix())
amplitude()(qubits[0], qubits[1], qubits[2])

circuit = qprogram.to_circ(include_matrices=True)
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s amplitude %s" % (sample.state, sample.amplitude))

circuit.display()