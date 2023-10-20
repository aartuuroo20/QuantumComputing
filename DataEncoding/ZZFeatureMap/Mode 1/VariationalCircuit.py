from qat.lang import Program, RY, CNOT
from qat.core import Variable


class VariationalCircuit:
    #Constructor
    def __init__(self):
        nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(nqubits)
        self.CreateVariationalCircuit()

    #Function that create the variational circuit
    def CreateVariationalCircuit(self):
        ListVarTheta = []
        for i in range(8):
            ListVarTheta.append(Variable("varTheta" + str(i)))

        RY(ListVarTheta[0])( self.qubits[0])
        RY(ListVarTheta[1])( self.qubits[1])
        CNOT( self.qubits[0],  self.qubits[1])
        RY(ListVarTheta[2])( self.qubits[0])
        RY(ListVarTheta[3])( self.qubits[1])
        CNOT( self.qubits[0],  self.qubits[1])
        RY(ListVarTheta[4])( self.qubits[0])
        RY(ListVarTheta[5])( self.qubits[1])
        CNOT( self.qubits[0],  self.qubits[1])
        RY(ListVarTheta[6])( self.qubits[0])
        RY(ListVarTheta[7])( self.qubits[1])

    #Function that display the circuit
    def DisplayCircuit(self):
        circuit = self.qprogram.to_circ()
        circuit.display()

