from qat.lang import Program, AbstractGate
from qat.qpus import get_default_qpu
from matrix import Matrix

matrix = Matrix()

program = Program()
nqubits = 2
ncbits = 2
qubits = program.qalloc(nqubits)
cbits = program.calloc(ncbits)

#We create the ZZFeatureMap and the VariationalCircuit and we add them to the program
newGate = AbstractGate("newGate", [], 2, matrix_generator=matrix.genMatrix())
newGate()(qubits[0], qubits[1])

#We create the circuit and we display it
circuit = program.to_circ()

qpu = get_default_qpu() #Creamos un ordenador quantico
job = circuit.to_job() #Creamos un trabajo
result = qpu.submit(job) #Cargamos el trabajo a la QPU

for sample in result:
        print("State %s amplitude %s" % (sample.state, sample.count))


