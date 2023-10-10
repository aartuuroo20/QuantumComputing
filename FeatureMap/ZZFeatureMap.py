from qat.lang.AQASM import Program, H, X
from qat.qpus import get_default_qpu

class ZZFeatureMap: 
    def __init__(self):
        qprogram = Program()
        nqubits = 2
        qubits=qprogram.qalloc(nqubits)

        H(qubits[0])
        H(qubits[1])

        X(qubits[1])

        circuit = qprogram.to_circ()
        circuit.display()

