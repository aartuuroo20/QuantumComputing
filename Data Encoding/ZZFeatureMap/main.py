import numpy as np

from qat.lang import Program, AbstractGate
from DataSet import DataSet
from ZZFeatureMap import ZZFeatureMap
from VariationalCircuit import VariationalCircuit

#We initialize the objects
dataset = DataSet()
dataset.Draw()
zzfmObject = ZZFeatureMap()
varCircuitObject = VariationalCircuit()

#We create a prorgram with 2 qubits
program = Program()
nqubits = 2
qubits = program.qalloc(nqubits)

#We create the ZZFeatureMap and the VariationalCircuit and we add them to the program
zzfm = AbstractGate("ZZFM", [], arity=2, matrix_generator=zzfmObject.CreateZZFeatureMap())
zzfm()(qubits[0], qubits[1])
varCircuit = AbstractGate("vCircuit", [], arity=2, matrix_generator=varCircuitObject.CreateVariationalCircuit())
varCircuit()(qubits[0], qubits[1])

#We create the circuit and we display it
circuit = program.to_circ()
circuit.display()














