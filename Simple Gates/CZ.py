from qat.lang.AQASM import Program, Z, X
from qat.qpus import get_default_qpu

#Cambia de signo a -1 cuando ambos qubits son 1 cambiando objetivo a de signo

# =======  BEGIN =========
# Declaramos un programa
qprogram = Program()

# Inicializamos el número de qubits y cbits
nqubits = 2

# =======  BODY =========
# Asignamos los qubits
qubits=qprogram.qalloc(nqubits)

X(qubits[0])
X(qubits[1])
Z.ctrl()(qubits[1], qubits[0]) #control, objetivo


# Exportamos este programa a un circuito cuántico
circuit = qprogram.to_circ()

# Visualizamos el circuito
circuit.display()

# Creamos una unidad de proceso cuántico
qpu = get_default_qpu()

# =======  BODY =========
# Creamos un job
job = circuit.to_job()

# Enviamos el job a la QPU
result = qpu.submit(job)

# Iteramos sobre el vector de estado para obtener la probabilidad
for sample in result:
    print("State %s probability %s with amplitude %s" % (sample.state, sample.probability, sample.amplitude))

