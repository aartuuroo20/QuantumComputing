import numpy as np

from qat.lang.AQASM import Program, H, X, PH
from DataSet import DataSet

class Circuit():
    #Constructor
    def __init__(self):
        self.nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(self.nqubits)

        self.CreateZZFeatureMap()
        self.X()
        self.DisplayCircuit()

    #Function that create the ZZFeatureMap
    def CreateZZFeatureMap(self):

        H(self.qubits[0])
        H(self.qubits[1])

        X(self.qubits[1])
        PH(2*(np.pi - DataSet().X[0][0]) * (np.pi - DataSet().X[0][1]))(self.qubits[1])
        H(self.qubits[1])
        X(self.qubits[1])

    def X(self):
        X(self.qubits[0])

    #Function that display the circuit
    def DisplayCircuit(self):
        circuit = self.qprogram.to_circ()
        circuit.display()




