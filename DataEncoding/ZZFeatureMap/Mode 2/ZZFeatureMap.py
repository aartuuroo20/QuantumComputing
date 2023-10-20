import numpy as np

from qat.lang.AQASM import Program, H, PH, CNOT
from qat.core import Variable


class ZZFeatureMap():
    #Constructor
    def __init__(self):
        nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(nqubits)
        self.CreateZZFeatureMap()

    #Function that create the ZZFeatureMap
    def CreateZZFeatureMap(self):
        ListVarData = []
        for i in range(2):
            ListVarData.append(Variable("varData" + str(i)))

        H(self.qubits[0])
        H(self.qubits[1])
        PH(2* ListVarData[0])(self.qubits[0])
        PH(2* ListVarData[1])(self.qubits[1])
        CNOT(self.qubits[0], self.qubits[1])
        PH(2*(np.pi - ListVarData[0]) * (np.pi - ListVarData[1]))(self.qubits[1])
        CNOT(self.qubits[0], self.qubits[1])
        H(self.qubits[0])
        H(self.qubits[1])
        PH(2* ListVarData[0])(self.qubits[0])
        PH(2* ListVarData[1])(self.qubits[1])
        CNOT(self.qubits[0], self.qubits[1])
        PH(2*(np.pi - ListVarData[0]) * (np.pi - ListVarData[1]))(self.qubits[1])
        CNOT(self.qubits[0], self.qubits[1])

    #Function that display the circuit
    def DisplayCircuit(self):
        circuit = self.qprogram.to_circ()
        circuit.display()


