import numpy as np

from qat.lang import Program, AbstractGate, CustomGate
from qat.qpus import get_default_qpu
from qat.interop.qiskit import qlm_to_qiskit
from matrix import Matrix

def genMatrix():
    a = 1/np.sqrt(2)

    matrix = np.array([[a,0,0,0],
              [0,1.,0,0],
              [a,0,1.,0],
              [0,0,0,1.]])
        
    def gram_schmidt_columns(X):
        Q, R = np.linalg.qr(X)
        return Q
    
    matrix_aux = gram_schmidt_columns(matrix)
    return matrix_aux

qprogram = Program()
nqubits = 2
qubits = qprogram.qalloc(nqubits)

basis = AbstractGate("basis", [], arity=2, matrix_generator=genMatrix())
basis()(qubits[0], qubits[1])

circuit = qprogram.to_circ()
circuit.display()


