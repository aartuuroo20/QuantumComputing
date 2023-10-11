from qat.lang import Program, RY, CSIGN, RZ

class VariationalCircuit:
    #Constructor
    def __init__(self):
        nqubits = 2
        self.qprogram = Program()
        self.qubits = self.qprogram.qalloc(nqubits)
        self.theta = self.qprogram.new_var(float, '\\theta')
        self.CreateVariationalCircuit()

    #Function that create the variational circuit
    def CreateVariationalCircuit(self):
        RY(self.theta)(self.qubits[0])
        RY(self.theta)(self.qubits[1])
        RZ(self.theta)(self.qubits[0])
        RZ(self.theta)(self.qubits[1])
        CSIGN(self.qubits[0], self.qubits[1])
        RY(self.theta)(self.qubits[0])
        RY(self.theta)(self.qubits[1])
        RZ(self.theta)(self.qubits[0])
        RZ(self.theta)(self.qubits[1])
        CSIGN(self.qubits[0], self.qubits[1])
        RY(self.theta)(self.qubits[0])
        RY(self.theta)(self.qubits[1])
        RZ(self.theta)(self.qubits[0])
        RZ(self.theta)(self.qubits[1])

    #Function that display the circuit
    def DisplayCircuit(self):
        circuit = self.qprogram.to_circ()
        circuit.display()

