import numpy as np

from qat.lang.AQASM import Program, H, X, CustomGate
from DataSet import DataSet
from ZZFeatureMap import ZZFeatureMap
from VariationalCircuit import VariationalCircuit

'''
dataset = DataSet()
dataset.Draw()

program = Program()
nqubits = 2
qubits = program.qalloc(nqubits)

X(qubits[0])
zzmf = ZZFeatureMap()
customGate = CustomGate(zzmf)


circuit = program.to_circ()
circuit.display()

'''

vc = VariationalCircuit()
vc.DisplayCircuit()













