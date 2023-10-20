import numpy as np

from qat.lang import Program, AbstractGate
from qat.qpus import get_default_qpu
from matrix import Matrix

matrix = Matrix()

qprogram = Program()
nqubits = 2
qubits = qprogram.qalloc(nqubits)

basis = AbstractGate("basis", [], arity=2, matrix_generator=matrix.genMatrix())
basis()(qubits[0], qubits[1])

circuit = qprogram.to_circ(include_matrices=True)
job = circuit.to_job()
result = get_default_qpu().submit(job)

for sample in result:
    print("State %s probability %s" % (sample.state, sample.probability))

circuit.display()


