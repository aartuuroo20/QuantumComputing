import numpy as np

from qat.lang import Program, AbstractGate, CustomGate
from qat.qpus import get_default_qpu
from qat.interop.qiskit import qlm_to_qiskit
from matrix import Matrix

def gram_schmidt_columns(X):
    Q, R = np.linalg.qr(X)
    return Q

a = 1/np.sqrt(2)

matrix = np.array([[a,0,0,0],
              [0,1.,0,0],
              [a,0,1.,0],
              [0,0,0,1.]])

U_unitary = gram_schmidt_columns(matrix)



qprogram = Program()
nqubits = 3
qubits = qprogram.qalloc(nqubits)

amplitude = AbstractGate("amplitude", [], arity=2, matrix_generator=U_unitary)
amplitude()(qubits[0], qubits[1])

circuit = qprogram.to_circ(include_matrices=True)
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s amplitude %s" % (sample.state, sample.amplitude))

circuit.display()
        



