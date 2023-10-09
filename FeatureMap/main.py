from PauliFeatureMap import PauliFeatureMap
from qat.lang.AQASM import Program


qubits = 2

qprog = Program()
nqbits = qprog.qalloc(qubits)

feature_map = PauliFeatureMap(feature_dimension=qubits, reps=2, entanglement='full', parameter_prefix='α',
                        paulis=['Z', 'YY', 'XZ'], insert_barriers=True)
              

qprog.apply(feature_map, nqbits)
print(qprog)
