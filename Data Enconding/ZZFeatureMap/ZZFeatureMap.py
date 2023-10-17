import numpy as np

from qat.lang.AQASM import Program, H, X, PH
from DataSet import DataSet

class ZZFeatureMap():
    #Function that create the ZZFeatureMap
    def CreateZZFeatureMap(self):
        nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(nqubits)

        H(self.qubits[0])
        H(self.qubits[1])

        X(self.qubits[1])
        PH(2*(np.pi - DataSet().X[0][0]) * (np.pi - DataSet().X[0][1]))(self.qubits[1])
        H(self.qubits[1])
        X(self.qubits[1])

    #Function that display the circuit
    def DisplayCircuit(self):
        circuit = self.qprogram.to_circ()
        circuit.display()




