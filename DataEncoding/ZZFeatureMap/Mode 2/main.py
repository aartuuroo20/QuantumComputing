from DataSet import DataSet
from Circuit import Circuit

dataset = DataSet()
dataset.Draw()
data = dataset.GetItems()

circuit = Circuit()
circuit.ZZFeatureMap()
circuit.varCircuit2()
circuit.display()

