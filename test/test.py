from qat.lang import Program, X, AbstractGate, H, PH
import numpy as np

from DataSet import DataSet


class Test():
    def create(self):
        nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(nqubits)

        H(self.qubits[0])
        H(self.qubits[1])

        X(self.qubits[1])
        PH(2*(np.pi - DataSet().X[0][0]) * (np.pi - DataSet().X[0][1]))(self.qubits[1])
        H(self.qubits[1])
        X(self.qubits[1])


        
        
